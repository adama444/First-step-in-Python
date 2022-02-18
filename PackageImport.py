import requests
import bs4


url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = bs4.BeautifulSoup(page.content, 'html.parser')

titres = soup.find_all("a", class_="gem-c-document-list__item-title")
for titre in titres:
    print(titre.string)

descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")
for description in descriptions:
    print(description.string)
