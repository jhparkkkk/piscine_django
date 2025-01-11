import sys
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://en.wikipedia.org/wiki/"
PHILOSOPHY_URL = "https://en.wikipedia.org/wiki/Philosophy"


def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


def find_first_link(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        content_div = soup.find("div", id="mw-content-text")
        if not content_div:
            return None

        paragraphs = content_div.find_all("p")
        for paragraph in paragraphs:
            links = paragraph.find_all("a", recursive=True)
            for link in links:
                if link.find_parent("i") or link.find_parent("em"):
                    continue
                if link.attrs.get("href", "").startswith("/wiki/") and ":" not in link.attrs.get("href", ""):
                    return BASE_URL + link.attrs["href"].lstrip("/").split("/")[1]

        return None
    except Exception as e:
        print(f"Error parsing HTML: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 roads_to_philosophy.py \"<search_term>\"")
        sys.exit(1)

    search_term = sys.argv[1]
    start_url = BASE_URL + search_term.replace(" ", "_")

    visited = []

    while True:
        if start_url in visited:
            print("infinitite loop")
            sys.exit(0)

        visited.append(start_url)
        if start_url == PHILOSOPHY_URL:
            print(
                f"{len(visited) - 1} roads from {visited[0].split('/')[-1].replace('_', ' ')} to philosophy!")
            for link in visited:
                print(link.split('/')[-1].replace('_', ' ').title())
            print(
                f"{len(visited) - 1} roads from {visited[0].split('/')[-1].replace('_', ' ')} to philosophy!")
            sys.exit(0)

        html = fetch_page(start_url)
        next_link = find_first_link(html)
        if not next_link:
            print("got stuck!")
            sys.exit(0)

        start_url = next_link


if __name__ == "__main__":
    main()
