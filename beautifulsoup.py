import requests
from bs4 import BeautifulSoup

url = "http://map.ngii.go.kr/ms/pblictn/koreaGrphBook.do"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")


main = soup.find(attrs={"class":"article depth1"}).text
contents = soup.find("ul", attrs={"class":"options koreanGeography"}).text
contents = contents.split("\n")[1:-1]

    
years = soup.find_all("h5")
cities = soup.find_all("h6")
title_lst = []
for year in years:
    for city in cities:
        for content in contents:
            title = year.get_text() + "년 " + city.get_text() + " " + content
            title_lst.append(title)

            
print(title_lst)

