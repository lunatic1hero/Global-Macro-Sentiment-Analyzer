"""AssetInsight — lightweight news sentiment analyzer."""
from .sentiment import AssetSentiment
from .web import WebInteractor
from .config import DEFAULTS

__all__ = ["AssetSentiment", "WebInteractor", "DEFAULTS"]
