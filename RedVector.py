# redvector.py
from utils.crawler import get_all_links
from utils.scanners import test_sqli, test_xss
from utils.logger import log_result
import os
from colorama import Fore, Style, init
import pyfiglet 

init(autoreset=True)

def print_banner():
    ascii_banner = pyfiglet.figlet_format("RedVector")
    print(Fore.RED + ascii_banner + Style.RESET_ALL)
    print(Fore.RED + "        Web Vulnerability Scanner\n" + Style.RESET_ALL)

def show_menu():
    print("""
1. Scan a URL
2. View Scan History
3. Clear Scan History
4. Exit
""")

def view_history():
    history_file = "scan_history/scan_history.txt"
    if os.path.exists(history_file):
        with open(history_file, "r") as f:
            history = f.read()
            if history.strip():
                print("=== Scan History ===")
                print(history)
            else:
                print("No scan history found.")
    else:
        print("No scan history found.")

def clear_history():
    history_file = "scan_history/scan_history.txt"
    if os.path.exists(history_file):
        os.remove(history_file)
        print("Scan history cleared.")
    else:
        print("No scan history to clear.")

def main():
    print_banner()
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            target_url = input("Enter target URL: ").strip()
            print("[*] Crawling links...")
            links = get_all_links(target_url)
            links.add(target_url)
            print(f"[*] Found {len(links)} links to scan.")

            for link in links:
                test_sqli(link)
                test_xss(link)
            print("[*] Scan completed.")

        elif choice == "2":
            view_history()
        elif choice == "3":
            clear_history()
        elif choice == "4":
            print("Exiting RedVector...")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
