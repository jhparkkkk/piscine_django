import requests
import dewiki
import sys


def fetch_wikipedia(query: str, language="fr") -> str:

    url = f"https://{language}.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "titles": query,
        "explaintext": True,
        "redirects": 1,
    }

    try:
        data = requests.get(url, params=params).json()

        pages = data["query"]["pages"]
        for page_id, page in pages.items():
            if page_id == "-1":
                return None
            return dewiki.from_string(page.get("extract"))
    except Exception as e:
        print(f"error fetching wikipedia : {e}")
        return None


def sanitize_filename(name: str) -> str:
    return name.replace(" ", "_").replace("/", "_")


def main():
    if len(sys.argv) != 2:
        print("requires 1 argument: the searched query")
        sys.exit(1)

    query = sys.argv[1]
    result = fetch_wikipedia(query)

    if not result:
        print(f"searched query not found : {query}")
        sys.exit(1)

    filename = f"{sanitize_filename(query)}.wiki"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(result)
    print(f"Saved to {filename}")


if __name__ == "__main__":
    main()
