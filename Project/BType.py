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



root = tk.Tk()
root.title("News Aggregator")
root.geometry("600x400")

# Label & Entry pentru subiect
label_subject = tk.Label(root, text="Subiect de căutare:")
label_subject.pack(pady=5)

entry_subject = tk.Entry(root, width=40)
entry_subject.pack(pady=5)

# Buton de căutare
button_search = tk.Button(root, text="Caută", command=search_news)
button_search.pack(pady=5)

# Zonă de text pentru afișarea știrilor
text_area = tk.Text(root, wrap=tk.WORD)
text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

# Rulează aplicația
root.mainloop()