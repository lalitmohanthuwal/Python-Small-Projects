import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from yt_dlp import YoutubeDL
import os
import sys

# Function to get the path to the bundled FFmpeg executable
def get_ffmpeg_path():
    # Determine the path to the bundled FFmpeg based on the operating system
    if sys.platform == "win32":
        ffmpeg_path = os.path.join("ffmpeg", "ffmpeg.exe")  # Windows
    else:
        ffmpeg_path = os.path.join("ffmpeg", "ffmpeg")  # macOS/Linux

    if not os.path.exists(ffmpeg_path):
        messagebox.showerror("Error", "FFmpeg not found! Please ensure it is bundled with the application.")
        return None
    return ffmpeg_path

# Function to fetch available video qualities
def fetch_qualities():
    url = url_entry.get()  # Get the URL from the user input

    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL!")
        return

    try:
        # Fetch available formats
        ydl = YoutubeDL()
        info_dict = ydl.extract_info(url, download=False)
        formats = info_dict.get('formats', None)

        if not formats:
            messagebox.showerror("Error", "No formats found for this video!")
            return

        # Extract available video qualities
        available_qualities = set()
        for f in formats:
            if f.get('height'):  # Check if the format has a height (video quality)
                available_qualities.add(f"{f['height']}p")

        # Sort qualities in descending order
        sorted_qualities = sorted(available_qualities, key=lambda x: int(x[:-1]), reverse=True)

        # Update the quality dropdown
        quality_dropdown['values'] = sorted_qualities
        quality_var.set(sorted_qualities[0])  # Set the default to the highest quality

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to download the video in the selected quality
def download_video():
    url = url_entry.get()  # Get the URL from the user input
    save_path = filedialog.askdirectory()  # Ask user for the save location
    selected_quality = quality_var.get()  # Get the selected quality from the dropdown

    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL!")
        return

    try:
        # Get the path to the bundled FFmpeg
        ffmpeg_path = get_ffmpeg_path()
        if not ffmpeg_path:
            return

        # Download the video in the selected quality
        ydl_opts = {
            'format': f'bestvideo[height<={selected_quality[:-1]}]+bestaudio/best[height<={selected_quality[:-1]}]',  # Select the best quality up to the selected resolution
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',  # Save path and filename
            'ffmpeg_location': ffmpeg_path,  # Use the bundled FFmpeg
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", f"Video downloaded successfully in {selected_quality} and saved at:\n{save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("500x350")  # Set the window size
root.configure(bg="#f0f0f0")  # Set background color

# Add a heading label
heading_label = tk.Label(root, text="YouTube Video Downloader", font=("Arial", 20, "bold"), bg="#f0f0f0")
heading_label.pack(pady=10)

# Add a label and entry for the YouTube URL
url_label = tk.Label(root, text="Enter YouTube URL:", font=("Arial", 12), bg="#f0f0f0")
url_label.pack(pady=5)

url_entry = tk.Entry(root, width=50, font=("Arial", 12))
url_entry.pack(pady=10)

# Add a button to fetch available qualities
fetch_button = tk.Button(root, text="Fetch Available Qualities", font=("Arial", 12), command=fetch_qualities, bg="#2196F3", fg="white")
fetch_button.pack(pady=10)

# Add a label for quality selection
quality_label = tk.Label(root, text="Select Video Quality:", font=("Arial", 12), bg="#f0f0f0")
quality_label.pack(pady=5)

# Add a dropdown menu for quality selection
quality_var = tk.StringVar()
quality_dropdown = ttk.Combobox(root, textvariable=quality_var, font=("Arial", 12), state="readonly")
quality_dropdown.pack(pady=10)

# Add a download button
download_button = tk.Button(root, text="Download Video", font=("Arial", 12), command=download_video, bg="#4CAF50", fg="white")
download_button.pack(pady=20)

# Run the app
root.mainloop()