# crawler.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_all_links(url):
    """Crawl a page and return all internal/external links"""
    links = set()
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        for a_tag in soup.find_all("a"):
            href = a_tag.get("href")
            if href:
                full_url = urljoin(url, href)
                links.add(full_url)
    except requests.RequestException:
        pass
    return links

def get_forms(url):
    """Extract all forms from a page"""
    forms = []
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        forms = soup.find_all("form")
    except requests.RequestException:
        pass
    return forms
