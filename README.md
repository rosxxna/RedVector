# RedVector  

**RedVector** is a terminal-based vulnerability scanner built in Python.  
It focuses on identifying common web application vulnerabilities such as **SQL Injection (SQLi)** and **Cross-Site Scripting (XSS)** using payloads and automated crawling.  

---

## Features  
- Detects **SQL Injection** vulnerabilities  
- Detects **XSS** vulnerabilities  
- Crawls target websites and extracts forms/links  
- Uses external payload files for extensibility (`payloads/`)  
- Stores scan history and results (`scan_history/scan_history.txt`)  
- Simple, terminal-based interface  

---

## Project Structure  

```
RedVector/
│
├── README.md              # Project description
├── requirements.txt       # Dependencies
├── redvector.py           # Main CLI scanner
│
├── payloads/              # Attack payloads
│   ├── sqli_payloads.txt
│   └── xss_payloads.txt
│
├── scan_history/          # Scan logs/results
│   └── scan_history.txt
│
├── utils/                 # Helper modules
│   ├── crawler.py
│   ├── scanners.py
│   └── logger.py
```

---

## Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/RedVector.git
   cd RedVector
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage  

Run the scanner:  
```bash
python redvector.py -u https://example.com
```

Options (coming soon):  
- `-u` : Target URL  
- `--sqli` : Run only SQL Injection tests  
- `--xss` : Run only XSS tests  

---

## Example  

```bash
python redvector.py -u https://testphp.vulnweb.com
```

Output:  
```
[+] Crawling target...
[+] Testing for SQL Injection...
[!] Potential vulnerability found at /login.php?id=1
```

---

## Requirements  
See [`requirements.txt`](requirements.txt) for Python package dependencies.  

---

## Disclaimer  
This tool is created **for educational and ethical testing purposes only**.  
Do **not** use RedVector on systems you do not own or have permission to test.  
The author is not responsible for any misuse.  
