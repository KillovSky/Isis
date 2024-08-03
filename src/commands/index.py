"""
Redireciona para a pasta commands.
"""

# Importa os requisitos
from typing import Any, Dict
from .cases.index import main as commands

# Define a função main
async def main(env: Dict[str, Any]):
    """Caso o comando redirecione para esse arquivo, redireciona ele de volta"""
    # Executa ela
    await commands(env)
