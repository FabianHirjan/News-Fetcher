import tkinter as tk

def search_news():
    """
    Function for Search button.
    """
    subject = entry_subject.get().strip()
    if not subject:
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, "Enter a subject to search.")
        return
    
    text_area.delete("1.0", tk.END)
    
    #news_list = get_all_news(subject)
    
    if not news_list:
        text_area.insert(tk.END, "Nu au fost găsite rezultate pentru subiectul introdus.\n")
    else:
        for idx, news_title in enumerate(news_list, start=1):
            text_area.insert(tk.END, f"{idx}. {news_title}\n\n")


def fetchGoogleNews():
    """
    Function to fetch news from Google News.
    """
    news_list = ["Google News 1", "Google News 2", "Google News 3"]
    return news_list

def fetchYahooNews():
    """
    Function to fetch news from Yahoo News.
    """
    news_list = ["Yahoo News 1", "Yahoo News 2", "Yahoo News 3"]
    return news_list

def fetchBingNews():
    """
    Function to fetch news from Bing News.
    """
    news_list = ["Bing News 1", "Bing News 2", "Bing News 3"]
    return news_list

root = tk.Tk()
root.title("News Aggregator")
root.geometry("600x400")

# Label & Entry for subject
label_subject = tk.Label(root, text="Subiect de căutare:")
label_subject.pack(pady=5)

entry_subject = tk.Entry(root, width=40)
entry_subject.pack(pady=5)

# search button
button_search = tk.Button(root, text="Caută", command=search_news)
button_search.pack(pady=5)

# Text area
text_area = tk.Text(root, wrap=tk.WORD)
text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

# Run the app
root.mainloop()