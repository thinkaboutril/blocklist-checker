Blocklist Checker

Overview

The Blocklist Checker is a Python-based application with a GUI built using Tkinter. It is designed to check whether domains listed in a hosts file are resolving or blocked by a DNS resolver. This tool helps users determine if their DNS configuration effectively blocks unwanted domains based on hosts file provided.
Features

    GUI Interface: Provides a user-friendly graphical interface using Tkinter.
    Hosts File Parsing: Reads the local hosts file to extract domain entries.
    DNS Resolution Check: Checks each domain against DNS servers to determine if it resolves.
    Output Results: Generates a text file report indicating whether each domain is resolved or blocked.
    Cross-Platform: Works on Windows, macOS, and Linux.

Usage

    Download: Download the latest release from the Releases page.

    Run the Application:
        On Windows: Double-click on the blocklist-checker.exe.
        On macOS/Linux: Run blocklist-checker from the terminal.

    GUI Instructions:
        Click on "Open Hosts File" to select the hosts file (hosts or hosts.txt) to analyze.
        Click on "Check DNS Blocklist" to start the analysis.
        Once the process completes, a report file (blocklist_report.txt) will be generated in the same directory.

Requirements

    Python 3.x
    Libraries: tkinter (usually comes with Python installation)

Installation from Source

To run the application from source, ensure you have Python 3.x installed and install the required dependencies:

bash

pip install -r requirements.txt

Clone the repository:

bash

git clone https://github.com/thinkaboutril/blocklist-checker.git
cd repo-name

Run the application:

bash

python blocklist-checker.py

Screenshots

Include screenshots of your application's GUI here to give users a preview.
Contributing

Contributions are welcome! Please fork the repository and submit a pull request.
License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

    Mention any libraries or resources you used here.

Contact

    Your Name - @your-twitter
    Project Link: https://github.com/your-username/repo-name
