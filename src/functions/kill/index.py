"""
Implementação de Envio de Mensagem Baileys do Python para NodeJS.
"""

# Importa os requisitos
import json
import warnings
from typing import Any, Dict
import requests
from urllib3.exceptions import InsecureRequestWarning
from src.indexer.index import config

# Suprimir avisos de SSL
warnings.simplefilter("ignore", InsecureRequestWarning)


def postmessage(url: str, data: Dict[str, Any], timeout: int = 10) -> requests.Response:
    """Envia uma requisição POST para o servidor usando requests.

    Args:
        url (str): A URL do servidor e o endpoint (por exemplo, "https://example.com/send").
        data (Dict[str, Any]): Dados a serem enviados no corpo da requisição POST.
        timeout (int): Tempo de espera para a requisição em segundos.

    Retorna:
        requests.Response: O objeto de resposta.
    """
    # Converte os dados para JSON
    json_data = json.dumps(data)

    # Try para capturar exceções
    try:
        # Envia a requisição POST
        response = requests.post(
            url,
            data=json_data,
            headers={"Content-Type": "application/json"},
            verify=False,
            timeout=timeout
        )

        # Verifica se houve erros na requisição
        response.raise_for_status()

        # Retorna a resposta
        return response

    # Captura exceções de RequestException
    except requests.RequestException as error:
        # Imprime o erro
        print(error)

        # Lança a exceção
        raise error


def sendraw(chatid: str, msg: Dict[str, Any], quoted: str, code: Any) -> Any:
    """Envia uma mensagem personalizada via requisição POST.

    Args:
        chatid (str): ID do chat.
        msg (Dict[str, Any]): Mensagem a ser enviada, funciona de maneira semelhante ao Baileys.
        quoted (str): Mensagem a ser citada.
        code (Any): Código JavaScript a ser executado.

    Retorna:
        data (Any): Geralmente é um JSON dos dados enviados com informações recebidas do NodeJS.
    """
    # Monta os dados da requisição
    post_data = {
        "username": config["Auth"]["value"]["username"],
        "password": config["Auth"]["value"]["password"],
        "code": code,
        "chatId": chatid,
        "quoted": quoted,
        "message": msg,
    }

    # Obtém a URL do servidor
    url = config["PostRequest"]["value"]

    # Envia a requisição POST e obtém a resposta
    data = postmessage(url, post_data)

    # Retorna os dados da resposta
    return data


def sendmessage(chatid: str, msg: Dict[str, Any], quoted: str, code: Any) -> Any:
    """Interface simples para enviar uma mensagem via requisição POST.

    Args:
        chatid (str): ID do chat.
        msg (Dict[str, Any]): Object da mensagem, funciona de maneira semelhante ao Baileys.
        quoted (str): Mensagem a ser citada.
        code (Any): Código JavaScript a ser executado.

    Retorna:
        data (Any): Geralmente é um JSON dos dados enviados com informações recebidas do NodeJS.
    """
    # Envia a mensagem personalizada
    data = sendraw(chatid, msg, quoted, code)

    # Retorna os dados da resposta
    return data
