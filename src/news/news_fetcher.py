import requests
from bs4 import BeautifulSoup
import click

def fetch_latest_news():
    google_news_url = "https://news.google.com/search?q=Minnesota+Vikings&hl=en-US&gl=US&ceid=US:en"
    
    click.echo("Minnesota Vikings Top Stories:")
    click.echo("-------------------------------")
    click.echo(f"URL: {google_news_url}")
    click.echo("(Control + Right Click to open the link in your browser)")
    click.echo("-------------------------------")

def display_links(links):
    click.echo("Latest Minnesota Vikings News Links:")
    click.echo("-------------------------------")
    
    for i, link in enumerate(links, 1):
        click.echo(f"{i}. {link}")
        click.echo("-------------------------------")

def main():
    fetch_latest_news()

if __name__ == "__main__":
    main()
