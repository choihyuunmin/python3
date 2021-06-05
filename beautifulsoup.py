import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

url = "http://map.ngii.go.kr/ms/pblictn/koreaGrphBook.do"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)
wait = WebDriverWait(browser, 10)



main = soup.find(attrs={"class":"article depth1"}).text

years = [year.get_text() for year in soup.find_all("h5", attrs={"class":"article depth2"})]
years.insert(1, '2015')
years.insert(2, '2014')
years.insert(3, '2014')
years.insert(-2, '2004')

cities = [city.get_text() for city in soup.find_all("h6",attrs={"class":"article depth3"})]
contents = [content.get_text().split("\n") for content in soup.find_all("ul",attrs={"class":"options koreanGeography"})]

title = []
for i in range(len(years)):
    contents[i] = [v for v in contents[i] if v]
    for j in range(len(contents[i])):
        title.append(main + " - " + years[i] + "년 <" + cities[i] + "> " + contents[i][j])
        



browser.get("")
time.sleep(1)
browser.get("") 


enroll = browser.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/div[2]/div[1]/div[4]/button")
enroll.click()

time.sleep(1)
select = Select(browser.find_element_by_id("sysSeq"))
select.select_by_value("41")
label = browser.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div[2]/div/table/tbody/tr[3]/td/div[2]/label')
label.click()


titlebox = browser.find_element_by_id("title")
titlebox.send_keys(title[0])
contentsbox = browser.find_element_by_id("description")
contentsbox.send_keys("한국지리지는 1960년대 이후 산업화와 도시화 과정에서 국토 공간상에 발생한 변화를 분석하고 설명하는 동시에 그에 따른 국토와 해당지역의 문제점을 성찰하여 국토개발, 학술진흥, 교육, 정책결정 등 모든 분야에 활용하기 위하여 편찬되었습니다.\n\n %s"%title[0])
keywordbox = browser.find_element_by_id("keyword")
keywordbox.send_keys("한국지리지, 지리지, 발간, 국토개발, 학술")
landing_page = browser.find_element_by_id("landingPage")
landing_page.send_keys("http://map.ngii.go.kr/ms/pblictn/koreaGrphBook.do")
conti = browser.find_element_by_id("btnSaveIng")
conti.click()
time.sleep(1)
popup = Alert(browser)
popup.accept()


for i in range(1,len(title)):
    titlebox = browser.find_element_by_id("title")
    titlebox.send_keys(title[i])
    contentsbox = browser.find_element_by_id("description")
    contentsbox.send_keys("한국지리지는 1960년대 이후 산업화와 도시화 과정에서 국토 공간상에 발생한 변화를 분석하고 설명하는 동시에 그에 따른 국토와 해당지역의 문제점을 성찰하여 국토개발, 학술진흥, 교육, 정책결정 등 모든 분야에 활용하기 위하여 편찬되었습니다.\n\n %s"%title[i])
    keywordbox = browser.find_element_by_id("keyword")
    keywordbox.send_keys("한국지리지, 지리지, 발간, 국토개발, 학술")
    landing_page = browser.find_element_by_id("landingPage")
    landing_page.send_keys("http://map.ngii.go.kr/ms/pblictn/koreaGrphBook.do")
    conti = browser.find_element_by_id("btnSaveIng")
    conti.click()
    time.sleep(2)
    popup = Alert(browser)
    popup.accept()