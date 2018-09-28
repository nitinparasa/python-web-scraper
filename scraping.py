import requests
from bs4 import BeautifulSoup

r=requests.get("http://pythonhow.com/example.html")
c=r.content
soup=BeautifulSoup(c,"html.parser")
cities=soup.find_all("div",{"class":"cities"})
for item in cities:
    print(item.find_all("p")[0].text)