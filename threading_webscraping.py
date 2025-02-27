import requests
from bs4 import BeautifulSoup
import threading
import time

# List of URLs to scrape
URLS = [
    "https://www.example.com",
    "https://www.python.org",
    "https://www.wikipedia.org",
    "https://www.github.com",
    "https://www.stackoverflow.com"
]


def fetch_content(url, results):
    """Fetch HTML content from a URL."""
    print(f"started - {url}")
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text()
            results[url] = text
        else:
            results[url] = ""
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        results[url] = ""
    print(f"completed - {url}")

def scrape_websites():
    """Scrape multiple websites using threading."""
    results = {}
    threads = []

    for url in URLS:
        thread = threading.Thread(target=fetch_content, args=(url, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results



def main():
    start_time = time.time()

    print("Starting web scraping...")
    scraped_data = scrape_websites()
    print("Web scraping completed.",scraped_data.keys())



if __name__ == "__main__":
    main()
