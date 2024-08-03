"""
Roda comandos básicos em formato similar a switch-case do NodeJS.
"""

# Importa requisitos
import json  # noqa: F401 pylint: disable=unused-import
from typing import Any, Dict
from src.functions.kill import sendmessage, sendraw
from src.initialize.index import config


def checkcase(command: str, name: str = '', onlycmd: bool = False, iscmd: bool = False) -> bool:
    """
    Função para checar comandos sem prefixo.

    Args:
        command (str): Comando a ser checado.
        name (str): Nome do comando a ser checado.
        onlycmd (bool): Se deve checar apenas o comando exato.
        iscmd (bool): Se é um comando.

    Returns:
        bool: Retorna True se o comando for encontrado, caso contrário, False.
    """
    # Verifica se o comando corresponde ao nome
    if (name in command and onlycmd is False) or \
       (command == name and onlycmd is True and iscmd is True):
        return True

    # Retorna False se não corresponder
    return False


async def main(env: Dict[str, Any]):
    """
    Função para executar comandos com base nos parâmetros fornecidos.

    Args:
        env (Dict[str, Any]): Informações da mensagem, dados do comando, envInfo, Node.js ou demais.
    """
    # Se caso der qualquer tipo de erro
    try:
        # Só executa se a env for uma Object
        if isinstance(env, dict):
            # Obtém parametros necessários
            chatid = env.get('chatId')
            isowner = env.get('isOwner', False)
            iscmd = env.get('isCmd', False)
            reply = env.get('reply', False)
            arg = env.get('arg')
            command = env.get('command')

            # Se não for comando, define a mensagem como comando, para sistema de No-Prefix
            if not iscmd:
                # Define o corpo da mensagem como comando
                command = env.get('body', '')

            # Testes de comando sem prefix
            if checkcase(command, 'pythontest123+@', False, iscmd) or \
               checkcase(command, 'python test 123 +@', False, iscmd) or \
               checkcase(command, 'PYTHON TEST 123 +@', False, iscmd):

                # Envia a mensagem e retorna os dados dela
                data = sendmessage(chatid, {'text': '✔️ OK!'}, reply, False)

                # Retorna a data
                return data

            # Se for comando de eval
            elif isowner and checkcase(command, 'evalpy', True, iscmd):
                # Envia a mensagem e retorna os dados dela
                # pylint: disable=eval-used
                eval(arg)

            # Se for comando e tiver permissão de uso raw
            elif iscmd and config["Cases"]["value"] is True:
                # Envia a mensagem como raw e retorna os dados dela
                data = sendraw(chatid, {'text': 'Esse comando não existe ainda!'}, reply, False)

                # Retorna a data
                return data

    # Trata os erros genéricos
    except Exception as error:
        # Imprime o erro
        print(error)

        # Lança a exceção
        raise error
