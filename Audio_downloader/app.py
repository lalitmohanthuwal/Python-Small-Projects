import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from yt_dlp import YoutubeDL
# Function to fetch available video qualities
def fetch_qualities():
    url = url_entry.get().strip()  # Get URL from user input

    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL!")
        return

    try:
        ydl_opts = {'quiet': True, 'noplaylist': True}  # Prevent fetching playlist info
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)

        formats = info_dict.get('formats', [])

        if not formats:
            messagebox.showerror("Error", "No formats found for this video!")
            return

        available_qualities = set()
        for f in formats:
            if f.get('height') and f.get('vcodec') != 'none':  # Exclude audio-only formats
                available_qualities.add(f"{f['height']}p")

        if not available_qualities:
            messagebox.showerror("Error", "No video qualities found!")
            return

        sorted_qualities = sorted(available_qualities, key=lambda x: int(x[:-1]), reverse=True)

        quality_dropdown['values'] = sorted_qualities
        quality_var.set(sorted_qualities[0])  # Set highest quality as default

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Function to download video (with audio)
def download_video():
    url = url_entry.get().strip()
    save_path = filedialog.askdirectory()
    selected_quality = quality_var.get()

    if not url or not save_path:
        messagebox.showerror("Error", "Please enter a YouTube URL and select a save location!")
        return

    try:
        ydl_opts = {
            'format': f'bestvideo[height<={selected_quality[:-1]}]+bestaudio/best',  # Best format with both video + audio
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',  # Ensure it downloads as a single file
            'postprocessors': []  # Remove FFmpeg dependency
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        messagebox.showinfo("Success", f"Video downloaded successfully in {selected_quality} at:\n{save_path}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("500x400")
root.configure(bg="#f0f0f0")

# Add a heading label
heading_label = tk.Label(root, text="YouTube Video Downloader", font=("Arial", 18, "bold"), bg="#f0f0f0")
heading_label.pack(pady=10)

# YouTube URL entry
url_label = tk.Label(root, text="Enter YouTube URL:", font=("Arial", 12), bg="#f0f0f0")
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=50, font=("Arial", 12))
url_entry.pack(pady=10)

# Fetch qualities button
fetch_button = tk.Button(root, text="Fetch Available Qualities", font=("Arial", 12), command=fetch_qualities, bg="#2196F3", fg="white")
fetch_button.pack(pady=10)

# Quality selection dropdown
quality_label = tk.Label(root, text="Select Video Quality:", font=("Arial", 12), bg="#f0f0f0")
quality_label.pack(pady=5)
quality_var = tk.StringVar()
quality_dropdown = ttk.Combobox(root, textvariable=quality_var, font=("Arial", 12), state="readonly")
quality_dropdown.pack(pady=10)

# Download button
download_video_button = tk.Button(root, text="Download Video", font=("Arial", 12), command=download_video, bg="#4CAF50", fg="white")
download_video_button.pack(pady=20)

# Run the app
root.mainloop()
