"""
Verifica por atualizações do Projeto Isis
"""

# Importa os módulos necessários
import json
import aiohttp
from src.indexer.index import systemload


async def checkupdates(timeout: int = 10) -> bool:
    """Obtém e compara a versão local do package.json com a versão remota de forma assíncrona."""
    try:
        # Carrega a função de cores
        colorfy = systemload('color')

        # Lê o arquivo package.json local
        with open('package.json', 'r', encoding='utf-8') as file:
            local_pack = json.load(file)

        # Define a mensagem e se precisa dar update
        update_message = f"{colorfy['colorprint']('[VERSION] ', 'cyan')}"
        should_update = True

        # Obtém a versão remota do package.json
        async with aiohttp.ClientSession() as session:
            async with session.get(
                'https://raw.githubusercontent.com/KillovSky/Isis/main/package.json',
                timeout=timeout
            ) as response:
                # Ativa sistema de erros 4XX - 5XX
                response.raise_for_status()

                # Aguarda como texto
                json_text = await response.text()

                # Converte em JSON
                remote_pack = json.loads(json_text)

        # Define a mensagem de update
        update_message = update_message + (
            f"{colorfy['colorprint']('ATUALIZAÇÃO DISPONÍVEL ', 'red')}"
            f"→ [{colorfy['colorprint'](remote_pack['version'], 'magenta')} ~ "
            f"{colorfy['colorprint'](remote_pack['build_name'].upper(), 'blue')} ~ "
            f"{colorfy['colorprint'](remote_pack['build_date'].upper(), 'yellow')}] | "
            f"{colorfy['colorprint'](remote_pack['homepage'], 'green')}"
        )

        # Compara as versões e outras informações
        if (local_pack['version'] == remote_pack['version'] and
            local_pack['build_date'] == remote_pack['build_date'] and
            local_pack['build_name'] == remote_pack['build_name']):

            # Define a mensagem
            update_message = update_message + (
                f"{colorfy['colorprint']('Valeu por me manter atualizada!', 'green')}"
            )

            # Define como atualizado
            should_update = False

    # Erro remoto
    except aiohttp.ClientError as e:
        print(f"Erro ao verificar a versão remota: {e}")
        update_message = (
            update_message +
            f"→ {colorfy['colorprint']('GITHUB FILE NOT ABLE FOR VERIFICATION...', 'red')}"
        )

    # Erro no JSON
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Erro ao ler o arquivo local: {e}")
        update_message = (
            update_message +
            f"→ {colorfy['colorprint']('LOCAL FILE NOT ABLE FOR VERIFICATION...', 'red')}"
        )

    # Ou random
    except Exception as error:
        # Exibe a mensagem de falha
        print(error)

        # Define a mensagem
        update_message = (
            update_message +
            f"→ {colorfy['colorprint']('UNKNOWN ERROR RECEIVED...', 'red')}"
        )

        # Faz evaluação do erro
        raise error

    # Printa a mensagem
    print(update_message)

    # Retorna a mensagem de update ou atualizado
    return should_update
