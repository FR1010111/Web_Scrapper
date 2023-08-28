import requests
from bs4 import BeautifulSoup

URL = "Here Give Your Websites Link...."

def scrape_news_titles(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        articles = soup.find_all("article")

        for article in articles:
            title = article.find("h2").get_text()
            print(title)
    else:
        print("Failed to retrieve the webpage.")

if __name__ == "__main__":
    scrape_news_titles(URL)

#FN1010111