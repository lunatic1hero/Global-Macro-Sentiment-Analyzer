# AssetInsight

AssetInsight is a lightweight news-driven sentiment analysis system designed to evaluate bullish, bearish, or neutral sentiment for any financial asset. The tool works by fetching news links, extracting readable article content, and using either an LLM (OpenAI GPT models) or a free keyword-based heuristic to determine sentiment. The project is a refactored and extended version of a news-sentiment analyzer with a cleaner module structure, caching, provider abstraction, and a command-line interface.

---

## Features

- Fetch news from Google News (default) or NewsAPI (optional)
- Extract readable webpage content using Readability and BeautifulSoup
- Classify sentiment using OpenAI GPT models
- Optional dry-run heuristic mode requiring no API key
- On-disk caching to reduce repeated downloads and LLM calls
- Modular provider architecture for adding new news sources
- Command-line interface for quick execution
- Clean code layout for extension and maintenance

---

## Installation

Clone and install:

```bash
git clone <your-repository-url>
cd <your-repository-directory>
pip install -e .
```

---

## Environment Setup

Set the OpenAI API key:

```bash
export OPENAI_API_KEY="your-openai-key"
```

Windows:

```cmd
set OPENAI_API_KEY=your-openai-key
```

You can use the dry-run heuristic mode without providing an API key.

---

## Python Usage Example

```python
from assetinsight import AssetSentiment

an = AssetSentiment(
    asset="Crude Oil",
    openai_key="your-openai-key"
)

sentiment = an.get_sentiment(date="2025-11-16")
print(sentiment)

report = an.produce_daily_report(date="2025-11-16", max_words=300)
print(report)
```

---

## Command-Line Usage

Basic sentiment classification:

```bash
assetinsight run --asset "Bitcoin" --date 2025-11-16
```

Dry-run mode (no API key required):

```bash
assetinsight run --asset "Tesla" --dry-run
```

---

## Project Structure

```txt
assetinsight/
    __init__.py
    sentiment.py
    web.py
    llm_client.py
    config.py
    providers/
        google_scraper.py
        newsapi_adapter.py
    utils/
        __init__.py
        cache.py
cli.py
tests/
    test_extract.py
setup.py
requirements.txt
README.md
CHANGELOG.md
```

---

## Configuration

Default configurations (`config.py`):

```python
DEFAULTS = {
    "MODEL": "gpt-4o",
    "MAX_LINKS": 6,
    "CACHE_DIR": Path.home() / ".assetinsight_cache",
    "NEWS_PROVIDER": None
}
```

Customizable parameters include:

- LLM model
- Number of news links
- Cache directory path
- Provider (Google scraper or NewsAPI)
- API keys via environment variables

---

## Providers

### Google Scraper (default)
- Scrapes Google News for article links.
- No API key required.
- May break if Google changes HTML layout.

### NewsAPI (optional)
- More stable, uses NewsAPI service.
- Requires a NewsAPI key.

Example usage:

```python
from assetinsight.providers import newsapi_adapter

an = AssetSentiment(
    asset="Gold",
    provider=newsapi_adapter,
    openai_key="your-openai-key"
)
```

---

## Dry-Run Mode

When no OpenAI API key is available or `dry_run=True` is passed, a keyword-based heuristic determines sentiment.

Positive keywords:
- rise
- up
- higher
- bull
- gain

Negative keywords:
- fall
- down
- lower
- bear
- loss

Output is one of:
- bullish
- bearish
- neutral

---

## Example Outputs

Sentiment result:

```text
bullish
```

Daily report example:

```text
Crude Oil experienced mixed market signals today, with several reports citing...
```

---

## Development

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest -q
```

---

## License

Apache-2.0 License.

---

## Changelog

### 0.2.0
- Renamed project to AssetInsight  
- Added provider abstraction, caching, CLI, tests  
- Refactored sentiment and web modules  
- Improved architecture and maintainability  

