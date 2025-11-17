import click
from .sentiment import AssetSentiment

@click.group()
def cli():
    """AssetInsight CLI"""
    pass

@cli.command()
@click.option("--asset", "-a", required=True, help="Asset name to analyze")
@click.option("--date", "-d", default=None, help="Date (YYYY-MM-DD)")
@click.option("--max-links", "-n", default=6, type=int)
@click.option("--dry-run/--no-dry-run", default=False)
@click.option("--openai-key", default=None)
def run(asset, date, max_links, dry_run, openai_key):
    """Fetch links and produce sentiment (prints result)."""
    ai = AssetSentiment(asset=asset, openai_key=openai_key)
    links = ai.fetch_links(date=date, nlinks=max_links)
    click.echo(f"Found {len(links)} links.")
    sentiment = ai.get_sentiment(date=date, use_llm=not dry_run, dry_run=dry_run)
    click.echo("Sentiment: " + str(sentiment))
