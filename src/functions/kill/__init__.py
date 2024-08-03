"""
Exporta as funções kill para os arquivos necessários.
"""

# Importa do arquivo atual
from .index import sendraw, sendmessage, config

# Exporta as funções
__all__ = ["sendraw", "sendmessage", "config"]
