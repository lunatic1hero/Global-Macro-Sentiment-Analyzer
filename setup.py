from setuptools import setup, find_packages

setup(
    name="assetinsight",
    version="0.2.0",
    description="AssetInsight — news-driven sentiment & daily reports for financial assets",
    long_description=open("README.md").read() if __import__("os").path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/KVignesh122/AssetNewsSentimentAnalyzer",
    author="KVignesh122 (adapted)",
    packages=find_packages(exclude=("tests",)),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "readability-lxml",
        "lxml",
        "tiktoken",
        "openai",
        "aiohttp",
        "click",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "assetinsight=assetinsight.cli:cli"
        ]
    },
    license="Apache-2.0",
)
