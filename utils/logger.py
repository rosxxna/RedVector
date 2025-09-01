# logger.py
from colorama import Fore, Style
import os

HISTORY_FILE = "scan_history/scan_history.txt"

# Ensure scan_history folder exists
os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)

def log_result(message, vuln_type=None):
    """
    Log message to terminal and save to scan history.
    vuln_type can be 'SQLi', 'XSS', etc. for coloring.
    """
    if vuln_type == "SQLi" or vuln_type == "XSS":
        print(f"{Fore.RED}[{vuln_type}] {message}{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}{message}{Style.RESET_ALL}")
    
    # Append to history file
    with open(HISTORY_FILE, "a") as f:
        f.write(f"[{vuln_type if vuln_type else 'INFO'}] {message}\n")
