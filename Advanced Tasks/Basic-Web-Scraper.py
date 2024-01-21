# Design a program that scrapes and prints headlines from a news website. (Requires: BeautifulSoup and requests libraries)

import requests
from bs4 import BeautifulSoup


def scrape_headlines(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.find_all('h1', class_='headline')
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def print_headlines(headlines):
    if headlines:
        print("Headlines:")
        for i, headline in enumerate(headlines, start=1):
            print(f"{i}- {headline}")


def main():
    BASE_URL = "https://www.bbc.com/news"
    headlines = scrape_headlines(BASE_URL)

    if headlines:
        print_headlines(headlines)


if __name__ == "__main__":
    main()