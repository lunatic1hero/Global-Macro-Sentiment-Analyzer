from pathlib import Path

DEFAULTS = {
    "MODEL": "gpt-4o",
    "MAX_LINKS": 6,
    "CACHE_DIR": Path.home() / ".assetinsight_cache",
    "NEWS_PROVIDER": None  # set to "newsapi" to enable NewsAPI adapter
}
