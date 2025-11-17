import hashlib, json
from pathlib import Path
from typing import Any

class SimpleCache:
    def __init__(self, cache_dir):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _key(self, text: str) -> str:
        return hashlib.sha256(text.encode("utf-8")).hexdigest()

    def get(self, key_text: str) -> Any:
        k = self._key(key_text)
        fp = self.cache_dir / f"{k}.json"
        if not fp.exists():
            return None
        try:
            return json.loads(fp.read_text(encoding="utf-8"))
        except Exception:
            return None

    def set(self, key_text: str, value: Any):
        k = self._key(key_text)
        fp = self.cache_dir / f"{k}.json"
        try:
            fp.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")
        except Exception:
            pass


