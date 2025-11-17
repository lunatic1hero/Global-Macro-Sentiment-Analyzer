import requests

def newsapi_search(query, date=None, nlinks=6, api_key=None):
    if not api_key:
        raise ValueError("newsapi key required")
    url = "https://newsapi.org/v2/everything"
    params = {"q": query, "pageSize": nlinks, "sortBy": "relevancy", "apiKey": api_key}
    if date:
        params["from"] = date
        params["to"] = date
    r = requests.get(url, params=params, timeout=10)
    data = r.json()
    links = [a["url"] for a in data.get("articles", [])]
    return links
