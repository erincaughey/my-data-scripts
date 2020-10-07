# Raw script - not notebook

from requests import get
from bs4 import BeautifulSoup

url = "https://scorecard.lcv.org/members-of-congress"

html = get(url)
search_soup = BeautifulSoup(html, 'html.parser')
tbl = search_soup.find(id="moc-list-table-data").findAll(class_='tableRow')

