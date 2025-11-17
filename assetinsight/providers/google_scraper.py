import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import time

def google_search_news(query: str, date=None, nlinks=6):
    q = quote_plus(query)
    url = f"https://www.google.com/search?q={q}&tbm=nws"
    headers = {"User-Agent": "Mozilla/5.0 (compatible; AssetInsight/0.2.0)"}
    r = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(r.text, "lxml")
    results = []
    for a in soup.select("a"):
        href = a.get("href")
        if not href:
            continue
        if "/url?q=" in href:
            link = href.split("/url?q=")[1].split("&sa=U")[0]
            if link.startswith("http"):
                results.append(link)
        if len(results) >= nlinks:
            break
    time.sleep(1)
    return list(dict.fromkeys(results))[:nlinks]
