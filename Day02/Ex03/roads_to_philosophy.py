import requests
from bs4 import BeautifulSoup
import re
import sys

def get_first_link(url):
    # Fetch the HTML content of the Wikipedia page
    page_content = get_page_content(url)
    soup = BeautifulSoup(page_content, 'html.parser')

    # Find the first valid link from the introduction paragraph
    first_link = None
    intro_paragraph = soup.find("div", class_="mw-parser-output").find("p")
    for link in intro_paragraph.find_all("a", href=True):
        href = link.get("href")
        if href.startswith("/wiki/") and not href.startswith("/wiki/Help:"):
            first_link = "https://en.wikipedia.org" + href
            break

    return first_link

def get_page_content(url):
    # Function to fetch and return the HTML content of a Wikipedia page
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    start_url = input("Enter the Wikipedia URL: ")
    visited_urls = set()
    current_url = start_url

    while True:
        if current_url in visited_urls:
            print("It leads to an infinite loop!")
            sys.exit(1)

        page_content = get_page_content(current_url)
        soup = BeautifulSoup(page_content, 'html.parser')

        # Find eventual redirection
        # Consider the main title of the page
        # Get the first valid link from the introduction paragraph
        # Implement these steps using BeautifulSoup
        next_url = get_first_link(current_url)

        # Add current URL to visited set
        visited_urls.add(current_url)

        # Check termination conditions
        if current_url == "https://en.wikipedia.org/wiki/Philosophy":
            print(f"{len(visited_urls)} roads from {start_url} to philosophy!")
            sys.exit(0)
        elif next_url is None:
            print("It's a dead end!")
            sys.exit(0)

        # Update current URL for the next iteration
        current_url = next_url

if __name__ == "__main__":
    main()
