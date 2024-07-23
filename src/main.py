import click
from src.news.news_fetcher import fetch_latest_news
from src.players.current_players import get_current_roster

@click.group()
def main():
    pass

@main.command()
def news():
    """Fetch and display the latest news."""
    fetch_latest_news()

@main.command()
def roster():
    """Display the current roster."""
    get_current_roster()

if __name__ == "__main__":
    main()
