import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pytube import YouTube, Playlist
import os

# Function to update progress bar
def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    progress_var.set(percentage_of_completion)
    root.update_idletasks()

# Function to download video
def download_video():
    url = url_entry.get()
    save_path = filedialog.askdirectory()
    
    if not url or not save_path:
        messagebox.showwarning("Input Error", "Please provide a valid URL and save path.")
        return

    try:
        yt = YouTube(url, on_progress_callback=progress_function)
        if download_type.get() == "Audio":
            stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
        else:  # Download the highest resolution video with audio
            stream = yt.streams.get_highest_resolution()

        progress_var.set(0)
        progress_bar.grid(row=3, columnspan=2, pady=10)  # Show progress bar
        stream.download(save_path)
        progress_bar.grid_remove()  # Hide progress bar
        messagebox.showinfo("Success", f"Downloaded '{yt.title}' successfully!")

    except Exception as e:
        progress_bar.grid_remove()  # Hide progress bar in case of error
        messagebox.showerror("Error", str(e))

# Function to download playlist
def download_playlist():
    url = url_entry.get()
    save_path = filedialog.askdirectory()
    
    if not url or not save_path:
        messagebox.showwarning("Input Error", "Please provide a valid URL and save path.")
        return

    try:
        playlist = Playlist(url)
        progress_bar.grid(row=3, columnspan=2, pady=10)  # Show progress bar
        for video in playlist.videos:
            yt = video
            yt.register_on_progress_callback(progress_function)
            if download_type.get() == "Audio":
                stream = video.streams.filter(only_audio=True).order_by('abr').desc().first()
            else:  # Download the highest resolution video with audio
                stream = video.streams.get_highest_resolution()

            progress_var.set(0)
            stream.download(save_path)
        
        progress_bar.grid_remove()  # Hide progress bar
        messagebox.showinfo("Success", f"Downloaded playlist '{playlist.title}' successfully!")

    except Exception as e:
        progress_bar.grid_remove()  # Hide progress bar in case of error
        messagebox.showerror("Error", str(e))

# Setup GUI
def main():
    global root, url_entry, download_type, progress_var, progress_bar
    root = tk.Tk()
    root.title("YouTube Downloader")

    tk.Label(root, text="YouTube URL:").grid(row=0, column=0, padx=10, pady=10)
    url_entry = tk.Entry(root, width=50)
    url_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="Download Type:").grid(row=1, column=0, padx=10, pady=10)
    download_type = tk.StringVar(value="Video")
    tk.Radiobutton(root, text="Video", variable=download_type, value="Video").grid(row=1, column=1, sticky=tk.W)
    tk.Radiobutton(root, text="Audio", variable=download_type, value="Audio").grid(row=1, column=1)

    tk.Button(root, text="Download Video", command=download_video).grid(row=2, column=0, padx=10, pady=10)
    tk.Button(root, text="Download Playlist", command=download_playlist).grid(row=2, column=1, padx=10, pady=10)

    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate", variable=progress_var)

    root.mainloop()

if __name__ == "__main__":
    main()
