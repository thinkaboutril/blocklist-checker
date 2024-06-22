import socket
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import time
import threading
import webbrowser

# Global flags
stop_flag = threading.Event()
pause_flag = threading.Event()

def check_domains(domains, progress_bar, percentage_label, count_label, current_domain_label, time_label):
    results = {}
    total_domains = len(domains)
    start_time = time.time()

    for i, domain in enumerate(domains):
        if stop_flag.is_set():
            progress_bar["value"] = 0  # Reset progress bar value to 0
            percentage_label.config(text="0.00%")  # Reset percentage label
            break

        while pause_flag.is_set():
            time.sleep(0.1)  # Pause the thread when pause_flag is set
        
        progress_bar["value"] = (i + 1) / total_domains * 100
        percentage_label.config(text=f"{progress_bar['value']:.2f}%")
        count_label.config(text=f"{i + 1}/{total_domains} domains resolved")
        current_domain_label.config(text=f"{domain}")
        
        # Progress time
        elapsed_time = time.time() - start_time
        avg_time_per_domain = elapsed_time / (i + 1)
        remaining_time = avg_time_per_domain * (total_domains - (i + 1))
        
        if elapsed_time < 3600:
            elapsed_str = f"Elapsed: {int(elapsed_time)}s"
        else:
            elapsed_str = f"Elapsed: {int(elapsed_time / 3600)}h {int((elapsed_time % 3600) / 60)}m"

        if remaining_time < 3600:
            remaining_str = f"Remaining: {int(remaining_time)}s"
        else:
            remaining_str = f"Remaining: {int(remaining_time / 3600)}h {int((remaining_time % 3600) / 60)}m"

        time_label.config(text=f"{elapsed_str}, {remaining_str}")
        

        root.update_idletasks()
        
        try:
            socket.gethostbyname(domain)
            results[domain] = '--> RESOLVED'
        except socket.gaierror:
            results[domain] = '--> BLOCKED'
    
    return results

def save_results(results, output_filename):
    with open(output_filename, 'w') as file:
        for domain, status in results.items():
            file.write(f"{domain}: {status}\n")

def select_input_file():
    input_file = filedialog.askopenfilename(title="Select Blocklist File", filetypes=[("Text files", "*.txt")])
    if input_file:
        input_file_entry.delete(0, tk.END)
        input_file_entry.insert(0, input_file)

def select_output_file():
    output_file = filedialog.asksaveasfilename(title="Save Report As", defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if output_file:
        output_file_entry.delete(0, tk.END)
        output_file_entry.insert(0, output_file)

def start_check():
    input_file = input_file_entry.get()
    output_file = output_file_entry.get()
    
    if not input_file:
        messagebox.showerror("Error", "Please select an host file.")
        return
    
    if not output_file:
        messagebox.showerror("Error", "Please locate report file.")
        return
    
    # Read the list of domains from the input file
    with open(input_file, 'r') as file:
        domains = file.readlines()
    
    domains = [domain.strip() for domain in domains]
    
    # Progress bar and labels
    progress_bar["value"] = 0
    percentage_label.config(text="0.00%")
    count_label.config(text=f"0/{len(domains)} domains resolved")
    current_domain_label.config(text="Resolving: ")
    time_label.config(text="Elapsed: 0s, Remaining: 0s")
    
    # Clear flags
    stop_flag.clear()
    pause_flag.clear()
    
    # Resolving domain in separate thread (for GUI responsiveness)
    thread = threading.Thread(target=check_and_save_domains, args=(domains, output_file))
    thread.start()

def check_and_save_domains(domains, output_file):
    results = check_domains(domains, progress_bar, percentage_label, count_label, current_domain_label, time_label)
    
    if not stop_flag.is_set():
        # Save the results
        save_results(results, output_file)
        messagebox.showinfo("Completed", f"Results saved to {output_file}")
    else:
        messagebox.showinfo("Stopped", "The operation was stopped.")

def stop_check():
    stop_flag.set()

def pause_check():
    if pause_flag.is_set():
        pause_flag.clear()
        pause_button.config(text="Pause")
    else:
        pause_flag.set()
        pause_button.config(text="Resume")

def open_hyperlink(event):
    webbrowser.open_new("https://github.com/thinkaboutril/blocklist-checker")

# Main window
root = tk.Tk()
root.title("Blocklist Checker 1.0")
root.resizable(False, False)  # Disable resizing

# Set colors (dark)
bg_color = "#2E2E2E"
fg_color = "#FFFFFF"
fg_link = "#40e0d0"
btn_color = "#444444"
entry_bg_color = "#3E3E3E"
entry_fg_color = "#FFFFFF"

root.configure(bg=bg_color)

# Function browse file GUI
def create_entry_with_browse(parent, label_text, button_text, button_command):
    frame = tk.Frame(parent, bg=bg_color)

    label = tk.Label(frame, text=label_text, bg=bg_color, fg=fg_color)
    label.pack(anchor="center", pady=2)

    entry = tk.Entry(frame, width=50, bg=entry_bg_color, fg=entry_fg_color)
    entry.pack(anchor="center", pady=2)

    button = tk.Button(frame, text=button_text, command=button_command, bg=btn_color, fg=fg_color)
    button.pack(anchor="center", pady=2)

    return frame, entry

# Host file selection
input_file_frame, input_file_entry = create_entry_with_browse(root, "Host File:", "Browse", select_input_file)
input_file_frame.pack(pady=5)

# Report file selection
output_file_frame, output_file_entry = create_entry_with_browse(root, "Save Report As:", "Browse", select_output_file)
output_file_frame.pack(pady=5)

# Frame for operation buttons
button_frame = tk.Frame(root, bg=bg_color)
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="Start", command=start_check, bg=btn_color, fg=fg_color)
start_button.pack(side=tk.LEFT, padx=5)
stop_button = tk.Button(button_frame, text="Stop", command=stop_check, bg=btn_color, fg=fg_color)
stop_button.pack(side=tk.LEFT, padx=5)
pause_button = tk.Button(button_frame, text="Pause", command=pause_check, bg=btn_color, fg=fg_color)
pause_button.pack(side=tk.LEFT, padx=5)

# Progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=5, anchor="center", fill="x")
style = ttk.Style(root)
style.theme_use('clam')
style.configure("TProgressbar", troughcolor=bg_color, background="green", thickness=20)

# Progress label
percentage_label = tk.Label(root, text="0.00%", bg=bg_color, fg=fg_color)
percentage_label.pack(pady=2, anchor="center")

time_label = tk.Label(root, text="Elapsed: 0s, Remaining: 0s", bg=bg_color, fg=fg_color)
time_label.pack(pady=2, anchor="w")

count_label = tk.Label(root, text="0/0 domains resolved", bg=bg_color, fg=fg_color)
count_label.pack(pady=2, anchor="w")

current_domain_label = tk.Label(root, bg=bg_color, fg=fg_color)
current_domain_label.pack(pady=2, anchor="w")

version_info_frame = tk.Frame(root, bg=bg_color)
version_info_frame.pack(pady=5, anchor="w")

# Version info
version_label = tk.Label(version_info_frame, text="Version 1.0", bg=bg_color, fg=fg_color)
version_label.pack(side=tk.LEFT, padx=(0, 5))

hyperlink_label = tk.Label(version_info_frame, text="More info", bg=bg_color, fg=fg_link, cursor="hand2")
hyperlink_label.pack(side=tk.LEFT)
hyperlink_label.bind("<Button-1>", open_hyperlink)

root.mainloop()
