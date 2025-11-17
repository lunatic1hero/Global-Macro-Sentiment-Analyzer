import os
import openai
import tiktoken

class LLMClient:
    def __init__(self, api_key=None, model="gpt-4o"):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key
        self.model = model

    def _count_tokens(self, text: str):
        try:
            enc = tiktoken.encoding_for_model(self.model)
        except Exception:
            enc = tiktoken.get_encoding("cl100k_base")
        return len(enc.encode(text))

    def get_sentiment(self, text: str, dry_run=False):
        if dry_run or not self.api_key:
            t = text.lower()
            score = 0
            for w in ["rise", "up", "higher", "bull", "gain"]:
                score += t.count(w)
            for w in ["fall", "down", "lower", "bear", "loss"]:
                score -= t.count(w)
            return "bullish" if score > 0 else "bearish" if score < 0 else "neutral"

        prompt = f"Classify the following article as bullish, bearish or neutral for the asset:\n\n{ text }\n\nReturn one word only."
        resp = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role":"user","content":prompt}],
            max_tokens=20,
            temperature=0.0
        )
        return resp.choices[0].message.content.strip().lower()
