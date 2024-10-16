**Overview**

This project is a **Python-based multi-threaded file downloader** that allows users to download large files efficiently by splitting them into multiple parts and downloading them concurrently. The application leverages **Tkinter** for the GUI and **requests** for HTTP requests. Once all parts are downloaded, they are merged into a single file. This project demonstrates the power of concurrency to improve download speeds and provide real-time user feedback.

**Features**

- **Graphical User Interface (GUI)** using Tkinter for easy interaction.
- **Multi-threaded Downloading** for faster downloads by splitting files into parts.
- **Progress Tracking** with a progress bar and thread-based speed monitoring.
- **File Merging** to combine downloaded parts into a single file.
- **Customizable File Extensions** based on user input.
- **Scalable** design with configurable thread and part management.

**Prerequisites**

- **Python 3.x** installed on your system.
- Required libraries:
  - **Tkinter** (for GUI)
  - **requests** (for HTTP requests)

Install required libraries:

pip install requests

**Usage Instructions**

1. **Run the Application**:

python multi_threaded_downloader.py

1. **Enter File URL**:  
    Provide the URL of the file you wish to download.
2. **Specify File Extension**:  
    Enter the desired extension for the downloaded file (e.g., 'pdf', 'zip').
3. **Start Download**:  
    Click the **Download** button to initiate the download process.
4. **Monitor Progress**:
    - View download progress in the **progress bar**.
    - Monitor download speed for each thread in the console.
5. **Download Completion**:
    - The status label will display **"Download Complete"** when the process finishes.
    - All parts are merged into a single file with the specified extension.

**Application Design**

**User Interface (UI)**

- Uses **Tkinter** for interactive elements:
  - **Label** and **Entry widget** for entering the URL.
  - **Entry widget** to specify the file extension.
  - **Progress bar** to show download status.
  - **Status label** for real-time feedback.

**Logic and Concurrency**

- The file is split into **four parts** for parallel downloading.
- **Threads** handle individual parts to optimize download speed.
- Tracks and displays download speed and progress for each part.
- **Combines** all parts into a single file upon completion.

**Implementation**

- **download_file**: Initializes variables and starts threads for downloading.
- **download_part**: Uses HTTP range requests to download file segments.
- **update_progress**: Periodically updates progress and status labels.
- **combine_parts**: Merges all downloaded parts into one file.

**Real-World Applications**

- **Large File Distribution**: Download software, games, or videos efficiently.
- **Cloud Storage**: Speed up downloading of personal files from cloud platforms.
- **Media Streaming**: Preload media content for smooth playback.
- **Software Updates**: Deliver patches and updates faster to users.
- **Digital Libraries**: Allow researchers to download large datasets quickly.

**Evaluation**

- **Concurrency**: Increases download speed through parallel threads.
- **Scalable Design**: Allows flexibility in the number of parts to download.
- **User Feedback**: Real-time progress bars and status messages.
- **Reliable**: Manages HTTP requests and threading efficiently to ensure stable downloads.

**Video Demonstration**

Check out a video demo of the application [here](https://youtu.be/r-z1V2GONaY).

**Contributing**

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch:

git checkout -b feature-name

1. Make your changes and commit:

git commit -m "Add feature description"

1. Push the changes:

git push origin feature-name

1. Create a **Pull Request**.

**License**

This project is licensed under the **MIT License**. See the LICENSE file for more details.

**Acknowledgments**

- **Tkinter** for the GUI framework.
- **requests** library for HTTP handling.
- Inspired by multi-threaded downloading techniques in software and media applications.
