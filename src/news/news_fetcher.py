import requests

def fetch_latest_news():
    # Example URL, replace with actual news API or RSS feed
    url = "https://api.example.com/vikings/news"
    response = requests.get(url)
    if response.status_code == 200:
        news = response.json()
        for article in news['articles']:
            print(f"{article['title']}\n{article['summary']}\n{article['url']}\n")
    else:
        print("Failed to fetch news.")
