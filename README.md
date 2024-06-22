
# Blocklist Checker

The Blocklist Checker is a Python-based application with a GUI built using Tkinter. It is designed to check whether domains listed in a hosts file are resolving or blocked by a DNS resolver. This tool helps users determine if their DNS configuration effectively blocks unwanted domains based on hosts file provided.


## Features

- GUI Interface: Provides a user-friendly graphical interface using Tkinter.
- Hosts File Parsing: Reads the local hosts file to extract domain entries.
- DNS Resolution Check: Checks each domain against DNS servers to determine if it resolves.
- Output Results: Generates a text file report indicating whether each domain is resolved or blocked.
- Cross-Platform: Works on Windows, macOS, and Linux.




## Usage
- Download: Download the latest release from the [Releases](https://github.com/thinkaboutril/blocklist-checker/releases/) page.
### Run the Application:
- **Windows:** Double-click on the blocklist-checker.exe.
- **macOS/Linux:** Run blocklist-checker from the terminal.
### GUI Instructions:
- Click **Browse** in the host file section to load the host file that the blocklist checker will be performed on. Example : [Blocklist Sample](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/domains/light.txt)
- Click **Browse** in the report file section to specify the directory to save the report file.
- Click **Start** to start the resolving process, click **Pause/Resume** to pause or resume the resolving process, click **Stop** to cancel the operation in progress.
- When the process is complete, you can see the checker results in the report file that has been determined at the previous step.







## Screenshots

![App Screenshot](https://i.postimg.cc/Gt23sjQX/Screenshot-2024-06-22-210521.png)



