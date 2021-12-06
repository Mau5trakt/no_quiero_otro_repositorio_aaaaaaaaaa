from bs4 import BeautifulSoup
import lxml

src = open("a.html")
document = BeautifulSoup(src, 'lxml')

ulist = document.find_all("td")

document.find(attrs={"td":"nowrap"})