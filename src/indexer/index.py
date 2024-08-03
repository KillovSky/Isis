"""
Módulo para carregamento de funções e comandos de forma modular.
"""

# Importa os módulos necessários
import importlib.util
import json
from pathlib import Path
from typing import Any, Dict, Union

# Constantes para os caminhos
SYMLINKS_PATH = Path(__file__).resolve().parent.parent.parent / 'src/settings/symlinks.json'
FUNCTIONS_DIR = Path(__file__).resolve().parent.parent.parent / 'src/functions'
COMMANDS_DIR = Path(__file__).resolve().parent.parent.parent / 'src/commands'
DEFAULT_COMMAND = 'cases'
DEFAULT_FUNCTION = 'fallback'

# Caminho para o arquivo de configuração
CONFIG_PATH = Path(__file__).resolve().parent.parent.parent / "src/settings/config.json"

# Configurações
config: Dict[str, Any] = {}
CONFIG_LOADED = False


def loadsettings() -> Dict[str, Any]:
    """
    Carrega as configurações de um arquivo JSON.
    
    Retorna:
        Dict[str, Any]: Configurações carregadas do arquivo JSON.
    """
    # pylint: disable=global-statement
    # Declara as variáveis globais CONFIG_LOADED e config
    global CONFIG_LOADED, config

    # Verifica se a configuração já foi carregada
    if CONFIG_LOADED:
        # Se sim, retorna o JSON já salvo
        return config

    # Verifica se o arquivo de configuração existe
    if not CONFIG_PATH.is_file():
        raise FileNotFoundError(f"Arquivo de configuração não encontrado: {CONFIG_PATH}")

    # Abre o arquivo de configuração
    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        # Carrega o conteúdo do arquivo JSON
        config = json.load(file)

        # Define CONFIG_LOADED como True
        CONFIG_LOADED = True

    # Retorna as configurações
    return config


def symlinks() -> Dict[str, Dict[str, Any]]:
    """
    Carrega o arquivo JSON de symlinks.
    
    Retorna:
        Dict[str, Dict[str, Any]]: O conteúdo do arquivo symlinks como um dicionário.
    """
    # Verifica se o arquivo de symlinks existe
    if SYMLINKS_PATH.is_file():
        # Abre o arquivo de symlinks
        with open(SYMLINKS_PATH, 'r', encoding='utf-8') as file:
            # Retorna o conteúdo do arquivo JSON
            return json.load(file)

    # Retorna um dicionário vazio se o arquivo não existir
    return {}


def systemload(data: Union[str, Dict[str, Any]]) -> Union[Dict[str, Any], bool]:
    """
    Recupera um comando pelo seu alias no arquivo 'symlinks.json' ou pelos nomes das pastas.
    Geralmente localizado em '/src/functions' ou '/src/commands'.
    
    Args:
        data (Union[str, Dict[str, Any]]): Dados da mensagem, que podem ser uma string ou um objeto.

    Retorna:
        Union[Dict[str, Any], bool]: O módulo de comando correspondente ou False se houver um erro.
    """
    try:
        # Define command_name como comando padrão
        command_name = DEFAULT_COMMAND
        # Se 'data' for uma string, trate-o como o nome do comando diretamente
        if isinstance(data, str):
            command_name = data.lower()

        # Se 'data' for um dicionário, extraia o nome do comando
        elif isinstance(data, dict):
            command_name = data.get('command', DEFAULT_COMMAND).lower()

        # Carrega os symlinks
        command_places = symlinks()

        # Verifica se command_places é um dicionário
        if not isinstance(command_places, dict):
            raise ValueError("O conteúdo do arquivo JSON de symlinks não é um dicionário válido.")

        # Inicializa a variável command_folder como None
        command_folder = None

        # Verifica se command_name é um diretório em COMMANDS_DIR ou FUNCTIONS_DIR
        if (COMMANDS_DIR / command_name).is_dir():
            command_folder = COMMANDS_DIR / command_name
        elif (FUNCTIONS_DIR / command_name).is_dir():
            command_folder = FUNCTIONS_DIR / command_name

        # Verifica nos symlinks
        else:
            # Percorre o JSON atrás de um correspondente
            for k, v in command_places.items(): # pylint: disable=unused-variable
                # Se tiver
                if command_name in v.get('alias', []):
                    # Define como o local dito no JSON
                    command_folder = Path(__file__).resolve().parent.parent.parent/Path(v['place'])

                    # Para o loop
                    break

        # Verifica se command_folder foi encontrado
        if not command_folder:
            # Define como diretório de comandos se isCmd existir no JSON
            if 'isCmd' in data:
                command_folder = COMMANDS_DIR / DEFAULT_COMMAND

            # Se não, determina como função
            else:
                command_folder = FUNCTIONS_DIR / DEFAULT_FUNCTION

        # Define o caminho do comando
        command_path = command_folder / 'index.py'

        # Verifica se o arquivo de comando existe
        if command_path.is_file():
            # Carrega o módulo do arquivo
            spec = importlib.util.spec_from_file_location(command_folder.name, command_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Obtém as funções do módulo
            functionsdata = {name: func for name, func in module.__dict__.items() if callable(func)}

            # Retorna as funções do módulo
            return functionsdata

        else:
            # Lança um erro se o arquivo de comando não for encontrado
            raise FileNotFoundError(f"Arquivo do módulo não encontrado em {command_path}")

    # Captura exceções
    except Exception as error:
        # Imprime o erro
        print(error)

        # Lança a exceção
        raise error


# Carrega a configuração JSON
loadsettings()
