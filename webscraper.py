import requests
from bs4 import BeautifulSoup
import csv
import argparse

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    headlines = []
    for heading in soup.find_all(['h1', 'h2', 'h3']):
        text = heading.get_text(strip=True)
        if text:
            headlines.append(text)
    return headlines

def save_to_csv(headlines, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Headline'])
        for headline in headlines:
            writer.writerow([headline])

def main():
    parser = argparse.ArgumentParser(description='Simple Web Scraper')
    parser.add_argument('url', type=str, help='URL of the website to scrape')
    parser.add_argument('--output', type=str, default='headlines.csv', help='Output CSV file (default: headlines.csv)')
    args = parser.parse_args()

    html = fetch_page(args.url)
    if html:
        headlines = parse_page(html)
        if headlines:
            save_to_csv(headlines, args.output)
            print(f"Headlines saved to {args.output}")
        else:
            print("No headlines found.")
    else:
        print("Failed to retrieve the webpage.")

if __name__ == "__main__":
    main()
