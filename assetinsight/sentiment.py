from .web import WebInteractor
from .llm_client import LLMClient
from .config import DEFAULTS

class AssetSentiment:
    def __init__(self, asset: str, openai_key=None, provider=None, cache_dir=None, model=None):
        self.asset = asset
        self.web = WebInteractor(cache_dir=cache_dir)
        # provider is a module-like object with .search or None
        if provider:
            self.web.provider = provider
        self.llm = LLMClient(api_key=openai_key, model=model or DEFAULTS["MODEL"])

    def fetch_links(self, date=None, nlinks=None):
        return self.web.get_links(query=self.asset, date=date, nlinks=nlinks or DEFAULTS["MAX_LINKS"])

    def fetch_articles(self, links):
        return [self.web.get_webpage_main_content(u) for u in links]

    def get_sentiment(self, date=None, use_llm=True, dry_run=False):
        links = self.fetch_links(date=date)
        contents = self.fetch_articles(links)
        merged = "\n\n".join([c for c in contents if c])
        if not use_llm:
            return self.llm.get_sentiment(merged, dry_run=True)
        return self.llm.get_sentiment(merged, dry_run=dry_run)

    def produce_daily_report(self, date=None, max_words=300, dry_run=False):
        links = self.fetch_links(date=date)
        articles = self.fetch_articles(links)
        merged = "\n\n".join([a for a in articles if a])
        if dry_run or not self.llm.api_key:
            # return short heuristic summary
            return f"Report (dry-run): {len(articles)} articles fetched for {self.asset}."
        prompt = f"Summarize the following articles about {self.asset} in {max_words} words:\n\n{merged}"
        # reuse llm client by sending prompt via ChatCompletion
        import openai
        resp = openai.ChatCompletion.create(
            model=self.llm.model,
            messages=[{"role":"user","content":prompt}],
            max_tokens=max_words + 50,
            temperature=0.2
        )
        return resp.choices[0].message.content.strip()
