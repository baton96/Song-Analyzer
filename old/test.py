import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import re
import time

chromeOptions = Options()
chromeOptions.headless = True
prefs = {'profile.managed_default_content_settings.images':2, 'disk-cache-size': 4096 }
chromeOptions.add_experimental_option("prefs", prefs)
driver = Chrome("chromedriver.exe", options=chromeOptions)
it = 0
times = []
for songLink in ['/piosenka,christina_aguilera,blank_page.html']:
    lyrics = ''
    tmpDict = {}
    
    try:
        driver.get("http://www.tekstowo.pl/piosenka,christina_aguilera,beautiful.html")
        soup= BeautifulSoup(driver.page_source, "html.parser")

        comments = soup.find_all('div', class_='desc')
        ratings = soup.find_all('div', class_='icons')
        
        for comment,rating in zip(comments,ratings):
            comment, rating = re.sub('\s+', ' ', comment.get_text()), re.sub('\s+', ' ', rating.get_text())       
            print(comment,rating)
        """
        lyrics = soup.find('div', class_='song-text').get_text().strip()
        lyrics = re.sub('\s+', ' ', lyrics)
        lyrics = re.search(r"Tekst piosenki: (.*) Poznaj histori", lyrics, re.MULTILINE)[1]
        lyrics = re.sub('\[.+?\]', '', lyrics)    
        

        #tmpDict['Tytuł'] = [songLink.get_text().split('-')[1].strip()]

        views = soup.find('div', class_='odslon')
        tmpDict['Odsłon'] = [views.get_text().split(': ')[1]]

        rank = soup.find('span', class_='rank')
        tmpDict['Punkty'] = [regexInt.search(rank.get_text())[0]]
        
        metric = soup.find('div', class_='metric')
        metric = metric.get_text()
        metric = metric.strip()
        metric = re.sub('\s\n', '\n', metric)
        metric = re.sub(' Edytuj metrykę', '', metric)
        metric = re.sub(' i inni', '', metric)
        metric = metric.split('\n')
        for i in metric:
            try:
                tmpDict[i.split(':')[0]]=i.split(':')[1].split(', ')
            except:
                pass
        """
    except:
        pass  
driver.quit()
