"""
Faz o print com cores no terminal.
"""

# Importa requisitos
import os
import logging
from typing import Optional

# Configuração básica de logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# Dicionário de cores ANSI
COLORS = {
    'reset': ['\033[0m', '\033[0m'],
    'bold': ['\033[1m', '\033[22m'],
    'dim': ['\033[2m', '\033[22m'],
    'italic': ['\033[3m', '\033[23m'],
    'underline': ['\033[4m', '\033[24m'],
    'inverse': ['\033[7m', '\033[27m'],
    'hidden': ['\033[8m', '\033[28m'],
    'strikethrough': ['\033[9m', '\033[29m'],
    'black': ['\033[30m', '\033[39m'],
    'red': ['\033[31m', '\033[39m'],
    'green': ['\033[32m', '\033[39m'],
    'yellow': ['\033[33m', '\033[39m'],
    'blue': ['\033[34m', '\033[39m'],
    'magenta': ['\033[35m', '\033[39m'],
    'cyan': ['\033[36m', '\033[39m'],
    'white': ['\033[37m', '\033[39m'],
    'gray': ['\033[90m', '\033[39m'],
    'grey': ['\033[90m', '\033[39m'],
    'brightRed': ['\033[91m', '\033[39m'],
    'brightGreen': ['\033[92m', '\033[39m'],
    'brightYellow': ['\033[93m', '\033[39m'],
    'brightBlue': ['\033[94m', '\033[39m'],
    'brightMagenta': ['\033[95m', '\033[39m'],
    'brightCyan': ['\033[96m', '\033[39m'],
    'brightWhite': ['\033[97m', '\033[39m'],
    'bgBlack': ['\033[40m', '\033[49m'],
    'bgRed': ['\033[41m', '\033[49m'],
    'bgGreen': ['\033[42m', '\033[49m'],
    'bgYellow': ['\033[43m', '\033[49m'],
    'bgBlue': ['\033[44m', '\033[49m'],
    'bgMagenta': ['\033[45m', '\033[49m'],
    'bgCyan': ['\033[46m', '\033[49m'],
    'bgWhite': ['\033[47m', '\033[49m'],
    'bgGray': ['\033[100m', '\033[49m'],
    'bgGrey': ['\033[100m', '\033[49m'],
    'bgBrightRed': ['\033[101m', '\033[49m'],
    'bgBrightGreen': ['\033[102m', '\033[49m'],
    'bgBrightYellow': ['\033[103m', '\033[49m'],
    'bgBrightBlue': ['\033[104m', '\033[49m'],
    'bgBrightMagenta': ['\033[105m', '\033[49m'],
    'bgBrightCyan': ['\033[106m', '\033[49m'],
    'bgBrightWhite': ['\033[107m', '\033[49m'],
    'blackBG': ['\033[40m', '\033[49m'],
    'redBG': ['\033[41m', '\033[49m'],
    'greenBG': ['\033[42m', '\033[49m'],
    'yellowBG': ['\033[43m', '\033[49m'],
    'blueBG': ['\033[44m', '\033[49m'],
    'magentaBG': ['\033[45m', '\033[49m'],
    'cyanBG': ['\033[46m', '\033[49m'],
    'whiteBG': ['\033[47m', '\033[49m']
}


def colorprint(text: Optional[str] = None, color: str = 'green') -> str:
    """
    Imprime uma mensagem no console com a cor especificada.

    Args:
        text (Optional[str]): Mensagem a ser impressa. Se None, exibe uma mensagem padrão.
        color (str): Nome da cor a ser usada para a mensagem.

    Returns:
        str: Mensagem formatada com a cor.
    """
    # Mensagem padrão
    default_message = (
        f"\033[31m[{os.path.basename(os.getcwd())}]\033[39m → "
        "\033[33mThe operation cannot be completed because no text has been sent.\033[39m"
    )

    # Adquire a cor ou usa uma padrão
    color = COLORS.get(color, COLORS['green'])

    # Se for uma string
    if isinstance(text, str):
        # Define como o texto usado
        formatted_message = f"{color[0]}{text}{color[1]}"

    # Caso contrário
    else:
        # Faz um aviso de erro
        logging.error("A mensagem deve ser uma string. Mensagem recebida: %s", text)

        # E define a mensagem padrão
        formatted_message = default_message

    # Retorna a string com cores
    return formatted_message
