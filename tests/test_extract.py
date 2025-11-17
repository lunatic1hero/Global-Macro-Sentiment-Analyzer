from assetinsight.web import WebInteractor

def test_simple_extraction(tmp_path):
    w = WebInteractor(cache_dir=tmp_path)
    html = "<html><body><article><h1>Title</h1><p>Rise and fall of asset</p></article></body></html>"
    url = "http://example.com/test"
    w.cache.set(url, html)
    out = w.get_webpage_main_content(url)
    assert "Rise and fall" in out
