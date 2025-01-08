import tkinter as tk
from gnews import GNews
import feedparser
import random
import requests

NEWSAPI_KEY = "a936290175ca43ae9a32847602b2e368"


def fetch_overall_news():
    """
    Fetch overall news from different sources.
    """
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, "Fetching news...\n\n")

    try:
        google_news_list = get_top_g_news()
        sky_news_list = get_sky_news()
        nyt_news_list = get_nyt_news()
        cnn_news_list = get_cnn_news()

        combined_news = google_news_list + sky_news_list + nyt_news_list + cnn_news_list
        random.shuffle(combined_news)

        for idx, news in enumerate(combined_news, start=1):
            title = news.get('title', 'No Title Available')
            source = news.get('source', 'Unknown Source')
            url = news.get('link', 'No URL Available')

            text_area.insert(
                tk.END,
                f"{idx}. {title}\nSource: {source}\nLink: {url}\n\n"
            )

    except Exception as e:
        text_area.insert(tk.END, f"An error occurred while fetching news: {e}\n")


def search_news():
    """
    Search by subject and fetch
    """
    subject = entry_subject.get().strip()
    if not subject:
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, "Enter a subject to search.")
        return

    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, f"Searching news for: {subject}\n\n")

    try:
        google_news_list = get_g_news(subject)
        sky_news_list = get_sky_news()
        nyt_news_list = get_nyt_news()
        cnn_news_list = get_cnn_news(subject)

        combined_news = google_news_list + sky_news_list + nyt_news_list + cnn_news_list
        random.shuffle(combined_news)

        if not combined_news:
            text_area.insert(tk.END, "No results found for the entered subject.\n")
        else:
            for idx, news in enumerate(combined_news, start=1):
                title = news.get('title', 'No Title Available')
                source = news.get('source', 'Unknown Source')
                url = news.get('link', 'No URL Available')

                text_area.insert(
                    tk.END,
                    f"{idx}. {title}\nSource: {source}\nLink: {url}\n\n"
                )

    except Exception as e:
        text_area.insert(tk.END, f"An error occurred while fetching news: {e}\n")


def get_g_news(subject):
    """
    Get Google News based on a subject.
    """
    google_news = GNews()
    news = google_news.get_news(subject)
    news_list = [
        {'title': item.get('title', 'No Title Available'), 
         'source': item.get('source', {}).get('name', 'Google News'), 
         'link': item.get('url', 'No URL Available')} for item in news
    ]
    return news_list


def get_top_g_news():
    """
    Get top Google News.
    """
    google_news = GNews()
    news = google_news.get_top_news()
    news_list = [
        {'title': item.get('title', 'No Title Available'), 
         'source': item.get('source', {}).get('name', 'Google News'), 
         'link': item.get('url', 'No URL Available')} for item in news
    ]
    return news_list


def get_sky_news():
    """
    Fetch Sky News RSS feed.
    """
    url = "https://feeds.skynews.com/feeds/rss/home.xml"
    feed = feedparser.parse(url)
    news_list = [
        {'title': entry.title, 'source': 'Sky News', 'link': entry.link} 
        for entry in feed.entries
    ]
    return news_list


def get_nyt_news():
    """
    Fetch New York Times RSS feed for Europe.
    """
    url = "https://rss.nytimes.com/services/xml/rss/nyt/Europe.xml"
    feed = feedparser.parse(url)
    news_list = [
        {'title': entry.title, 'source': 'New York Times', 'link': entry.link} 
        for entry in feed.entries
    ]
    return news_list


def get_cnn_news(subject=None):
    """
    Fetch CNN news using NewsAPI.
    """
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": NEWSAPI_KEY,
        "sources": "cnn",
        "q": subject if subject else None,
        "language": "en",
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])
        news_list = [
            {'title': article.get('title', 'No Title Available'),
             'source': 'CNN',
             'link': article.get('url', 'No URL Available')}
            for article in articles
        ]
        return news_list
    else:
        return []



root = tk.Tk()
root.title("GUI News Feed")
root.geometry("600x400")

# Label & Entry for subject
label_subject = tk.Label(root, text="Search Subject:")
label_subject.pack(pady=5)

entry_subject = tk.Entry(root, width=40)
entry_subject.pack(pady=5)

# Search button
button_search = tk.Button(root, text="Search", command=search_news)
button_search.pack(pady=5)

# Text area
text_area = tk.Text(root, wrap=tk.WORD)
text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

fetch_overall_news()

root.mainloop()
