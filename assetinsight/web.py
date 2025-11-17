import requests
from readability import Document
from bs4 import BeautifulSoup
from .utils.cache import SimpleCache
from .config import DEFAULTS

class WebInteractor:
    def __init__(self, cache_dir=None):
        self.cache = SimpleCache(cache_dir or DEFAULTS["CACHE_DIR"])
        self.provider = None

    def _fetch_sync(self, url):
        cached = self.cache.get(url)
        if cached:
            return cached
        r = requests.get(url, timeout=15, headers={"User-Agent":"Mozilla/5.0 (AssetInsight/0.2.0)"})
        raw = r.text
        self.cache.set(url, raw)
        return raw

    def get_webpage_main_content(self, url):
        raw = self._fetch_sync(url)
        doc = Document(raw)
        summary = doc.summary()
        soup = BeautifulSoup(summary, "lxml")
        txt = soup.get_text(separator="\n", strip=True)
        return txt

    def get_links(self, query, date=None, nlinks=DEFAULTS["MAX_LINKS"]):
        if self.provider:
            return self.provider.search(query=query, date=date, nlinks=nlinks)
        from .providers.google_scraper import google_search_news
        return google_search_news(query=query, date=date, nlinks=nlinks)
