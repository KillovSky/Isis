"""
Módulo de fallback onde caem as requisições que não tem função projetada.
"""

def main(data: str) -> str:
    """
    Função default para caso alguma requisição não registrada caia aqui.
    Args:
        data (str): Nome da função que queria usar.
    Retorna:
        str: Mensagem de aviso.
    """
    # Posta que a função não existe
    print(f'Function {data} does not exist.')
