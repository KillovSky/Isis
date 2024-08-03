"""
Exporta a função de inicialização.
"""

# Importa do arquivo atual
from src.indexer.index import systemload, config, loadsettings

# Exporta as funções
__all__ = ["systemload", "loadsettings", "config"]
