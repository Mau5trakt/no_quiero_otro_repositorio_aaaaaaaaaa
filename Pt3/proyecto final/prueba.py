from bs4 import BeautifulSoup
import requests_html
from requests_html import HTMLSession

url = "https://www.geeksforgeeks.org/"

sesion = HTMLSession()
html_content = sesion.get(url).text

soup = BeautifulSoup(html_content, "html.parser")

texts = soup.find_all('p')
for text in texts:
    print(text.get_text())