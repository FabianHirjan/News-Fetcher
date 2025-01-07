import tkinter as tk
from gnews import GNews

def search_news():
    """
    Function for the Search button.
    """
    subject = entry_subject.get().strip()
    if not subject:
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, "Enter a subject to search.")
        return
    
    text_area.delete("1.0", tk.END)
    
    try:
        news_list = get_g_news(subject)
    except Exception as e:
        text_area.insert(tk.END, f"An error occurred while fetching news: {e}\n")
        return

    if not news_list:
        text_area.insert(tk.END, "No results found for the entered subject.\n")
    else:
        for idx, news in enumerate(news_list, start=1):
            title = news.get('title', 'No Title Available')
            source = news.get('source', {}).get('name', 'Unknown Source')
            url = news.get('url', 'No URL Available')
            
            text_area.insert(
                tk.END,
                f"{idx}. {title}\nSource: {source}\nLink: {url}\n\n"
            )


def get_g_news(subject):
    """
    Function to get Google News based on a subject.
    """
    google_news = GNews()
    news = google_news.get_news(subject)
    return news

def get_top_g_news():
    """
    Function to get top Google News.
    """
    google_news = GNews()
    return google_news.get_top_news()

root = tk.Tk()
root.title("News Aggregator")
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

root.mainloop()
