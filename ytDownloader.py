import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
from sys import argv

def download_video():
    link = link_entry.get()
    try:
        yt = YouTube(link)
        yd = yt.streams.get_highest_resolution()
        yd.download('./vids')
        messagebox.showinfo("Download Complete", "Video downloaded successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Clears URL link
def clear_link():
    link_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create and place widgets
link_label = tk.Label(root, text="Enter YouTube Link:")
link_label.pack()

link_entry = tk.Entry(root, width=40)
link_entry.pack()

download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()

clear_button = tk.Button(root, text="Clear Link", command=clear_link)
clear_button.pack()

# Start the GUI event loop
root.mainloop()
