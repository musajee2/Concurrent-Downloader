import tkinter as tk
from tkinter import ttk
import requests
import threading
import os
import time

# Defining the download File function
def download_file():
    # Initializing Global Variables
    global data_parts, part_progress, bandwidth_info, progress_info

    # Getting the file URL from the entry widget
    global file_url
    file_url = url_entry.get()

    # Disabling the download button
    download_button.config(state=tk.DISABLED)

    # Initializing data_parts, part_progress, bandwidth_info, and progress_info lists
    data_parts = [None] * total_parts
    part_progress = [0] * total_parts
    bandwidth_info = [None] * total_parts
    progress_info = [0] * total_parts

    # Creating threads for downloading parts
    threads = []
    file_size = int(requests.head(file_url).headers.get('Content-Length', 0))
    part_size = file_size // total_parts

    # Starting Threads to Download it's specified part
    for i in range(total_parts):
        start_byte = i * part_size
        end_byte = start_byte + part_size - 1 if i < total_parts - 1 else file_size - 1
        thread = threading.Thread(target=download_part, args=(start_byte, end_byte, i))
        threads.append(thread)
        thread.start()

    # Starting updating progress
    update_progress()

# Defining the function which downloads the specified part of the file
def download_part(start_byte, end_byte, part_number):
    headers = {'Range': f'bytes={start_byte}-{end_byte}'}
    response = requests.get(file_url, headers=headers, stream=True)

    part_data = bytearray()
    start_time = time.time()
    total_bytes = 0

    for chunk in response.iter_content(chunk_size=8192):
        if chunk:
            part_data.extend(chunk)
            total_bytes += len(chunk)

            # Calculating download speed
            elapsed_time = time.time() - start_time
            if elapsed_time > 0:
                download_speed = total_bytes / elapsed_time / 1024  # in KB/s
                bandwidth_info[part_number] = f"Thread {part_number + 1}: {download_speed:.2f} KB/s"
                progress_info[part_number] = total_bytes

    data_parts[part_number] = part_data
    part_progress[part_number] = 100  # Marking the part as 100% complete

# Defining the function which updates the progress bar
def update_progress():
    total_progress = sum(part_progress) // total_parts
    progress_var.set(total_progress)

    for i in range(total_parts):
        if bandwidth_info[i] is not None:
            print(bandwidth_info[i], f"{progress_info[i] / 1024 / 1024:.2f} MB downloaded")

    if total_progress < 100:
        root.after(1000, update_progress)  # Update progress every second
    else:
        combine_parts()  # Combine parts when download is complete
        download_status.set("Download Complete")
        download_button.config(state=tk.NORMAL)

def combine_parts():
    with open(f"downloaded_file.{file_extension}", "wb") as full_file:
        for part_data in data_parts:
            full_file.write(part_data)

# Create the main window
root = tk.Tk()
root.title("Multi-Threaded File Downloader")

# Create and place widgets
url_label = tk.Label(root, text="Enter the desired File URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

extension_label = tk.Label(root, text="File Extension (e.g., 'zip', 'pdf', 'jpg'):")
extension_label.pack(pady=5)

extension_entry = tk.Entry(root, width=10)
extension_entry.pack(pady=5)

download_button = tk.Button(root, text="Download", command=download_file)
download_button.pack(pady=10)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.pack(fill=tk.X, padx=10, pady=5)

download_status = tk.StringVar()
status_label = tk.Label(root, textvariable=download_status)
status_label.pack(pady=10)

# Defining the number of parts for the file
total_parts = 4

# Initializing variables for file size and part size
file_size = 0
part_size = 0

# Defining the global variable for the file URL
file_url = ""

# Initializing lists for downloaded parts, progress, and bandwidth
data_parts = [None] * total_parts
part_progress = [0] * total_parts
bandwidth_info = [None] * total_parts
progress_info = [0] * total_parts

root.mainloop()
