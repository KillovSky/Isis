"""
Faz a parte de conexão do Projeto Íris.
"""

# Importa os módulos que forem necessários
import asyncio
import base64
import json
import logging
import signal
import ssl
import threading
from typing import Dict, NoReturn
import websocket
from src.indexer.index import config, loadsettings, systemload

# Desliga se mandar o sinal de close
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Importa a função de versão
upgrader = systemload('update')

# Verifica por updates
asyncio.run(upgrader['checkupdates']())


async def versioncheck(updater) -> NoReturn:
    """Executa a verificação de updates a cada X segundos."""
    # Faz em loop
    while True:
        # Aguarda X segundos antes de executar de novo
        await asyncio.sleep(config['UpdateInterval']['value'])

        # Com try, caso tenha erros
        try:
            # Executa a primeira vez
            await updater['checkupdates']()

        # Se der erro
        except Exception as e:
            # Printa ele
            print(e)

            # Faz a evaluação o erro
            raise e


def configure_logging() -> None:
    """Configura o logging do sistema."""
    # Configura o logging com nível de informação e formato de mensagem
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


async def process_message(ws: websocket.WebSocketApp, message: str) -> None:
    """Processa as mensagens recebidas do WebSocket.

    Args:
        ws (websocket.WebSocketApp): Objeto WebSocket.
        message (str): Mensagem recebida do WebSocket.
    """
    try:
        # Carrega a mensagem JSON
        data = json.loads(message)

        # Carrega as funções do sistema
        listfunctions = systemload(data)

        # Executa a função principal das funções carregadas
        await listfunctions['main'](data)

        # Define a função de cores
        colorfy = systemload('color')

        # Verifica se o tipo de requisição é 'log' e retorna o valor associado
        if 'printerMessage' in data:
            # Imprime a mensagem da impressora
            return print(data['printerMessage'])

        # Se não tiver usando a Íris recente (ou ainda não tiver a feature printerMessage)
        # E for comando
        elif 'isCmd' in data:
            # Se for comando
            if data['isCmd'] is True:
                # Imprime mensagem de comando
                return print(
                    colorfy['colorprint']("[LEGACY MODE ~ COMANDO]", "red"),
                    data['command']
                )

            # Mensagem normal
            else:
                # Imprime mensagem comum
                return print(
                    colorfy['colorprint']("[LEGACY MODE ~ MENSAGEM]", "red"),
                    data['body']
                )

            # Se não for uma mensagem do WhatsApp, cai nesse else.
        elif 'startlog' not in data:
            # Retorna uma mensagem padrão se o tipo não for uma mensagem da Íris
            return print(
                colorfy['colorprint']("Unknown Response:", "red"),
                data
            )

    # Erro ao abrir o JSON
    except json.JSONDecodeError as exc:
        # Loga o erro de decodificação de JSON
        logging.error("Erro ao decodificar JSON: %s", exc)

    # Erro generico
    except Exception as exc:
        # Loga a exceção genérica
        logging.exception("Erro ao processar a mensagem: %s", exc)

        # Lança a exceção
        raise exc

    # Retorna o websocket
    return ws


def on_message(ws: websocket.WebSocketApp, message: str) -> None:
    """Callback síncrono para processar as mensagens recebidas do WebSocket."""
    # Executa a função process_message de forma assíncrona
    asyncio.run(process_message(ws, message))

    # Retorna o websocket
    return ws


def on_error(ws: websocket.WebSocketApp, error: Exception) -> None:
    """Processa erros ocorridos durante a conexão WebSocket.

    Args:
        ws (websocket.WebSocketApp): Objeto WebSocket.
        error (Exception): Erro recebido.
    """
    # Loga o erro do WebSocket
    logging.error("Erro WebSocket: %s", error)

    # Retorna o websocket
    return ws


def on_close(ws: websocket.WebSocketApp, close_status_code: int, close_msg: str) -> None:
    """Notifica quando a conexão WebSocket é fechada.

    Args:
        ws (websocket.WebSocketApp): Objeto WebSocket.
        close_status_code (int): Código de status do fechamento.
        close_msg (str): Mensagem de fechamento.
    """
    # Loga o fechamento do WebSocket com o código e mensagem de fechamento
    logging.info("WebSocket fechou com code '%d': %s", close_status_code or 1, close_msg)

    # Retorna o websocket
    return ws


def on_open(ws: websocket.WebSocketApp) -> None:
    """Notifica quando a conexão WebSocket é aberta."""
    # Define o colorfy
    colorfy = systemload('color')

    # Loga a abertura da conexão WebSocket
    print(
        f"{colorfy['colorprint']('[START] ', 'green')}"
        f"{colorfy['colorprint']('→ Tudo pronto para começar!', 'yellow')}"
    )

    # Retorna o websocket
    return ws


def connect(ws_url: str, auth: Dict[str, str]) -> None:
    """Conecta ao WebSocket e inicia o loop de eventos.

    Args:
        ws_url (str): URL do WebSocket.
        auth (Dict[str, str]): Dicionário contendo as credenciais de autenticação.
    """
    # Codifica as credenciais em base64
    credentials = f"{auth['username']}:{auth['password']}"
    credentials_encoded = base64.b64encode(credentials.encode('utf-8')).decode('ascii')

    # Configura os headers de autenticação
    headers = {"Authorization": f"Basic {credentials_encoded}"}

    # Cria o objeto WebSocketApp
    ws = websocket.WebSocketApp(
        ws_url,
        header=headers,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )

    # Define a função de callback para a abertura do WebSocket
    ws.on_open = on_open

    # Inicia o loop de eventos do WebSocket com opções de SSL
    ws_thread = threading.Thread(target=ws.run_forever, kwargs={
        "sslopt": {"cert_reqs": ssl.CERT_NONE}
    })
    ws_thread.start()

    # Inicia o loop de atualizações periódicas
    asyncio.run(versioncheck(upgrader))


def initialize() -> None:
    """Função principal para leitura de configuração e início da conexão com o WebSocket."""
    # Carrega as configurações
    loadsettings()

    # Configura o logging
    configure_logging()

    # Try para caso der algum erro de função
    try:
        # Obtém a URL do WebSocket da configuração
        ws_url = config['WebSocket']['value']

        # Obtém as credenciais de autenticação da configuração
        auth = config['Auth']['value']

        # Importa e configura a função de atualização
        # pylint: disable=global-statement
        global upgrader
        upgrader = systemload('update')

        # Conecta ao WebSocket
        connect(ws_url, auth)

    # Captura exceções de KeyError
    except KeyError as exc:
        # Loga o erro ao acessar a configuração
        logging.error("Erro ao acessar configuração: %s", exc)

    # Captura exceções genéricas
    except Exception as exc:
        # Loga a exceção genérica
        logging.exception("Erro ao inicializar o projeto: %s", exc)

        # Lança a exceção
        raise exc


# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    # Inicializa a conexão com o WebSocket
    initialize()
