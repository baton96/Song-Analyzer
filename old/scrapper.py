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
bandName = "Billie_Eilish"
it=1
bandLinks = []
'''
while(True):
    driver.get("http://www.tekstowo.pl/szukaj,wykonawca,%s,strona,%d.html"% (bandName,it))
    soup= BeautifulSoup(driver.page_source, "html.parser")    
    it += 1    
    arr = list(filter(lambda x: x.get("href").startswith("/piosenki_artysty,"), soup.find_all('a')))
    if(len(arr)==0):
        break
    bandLinks += arr
regexInt = re.compile('-?\d+')
bandCounts = list(map(lambda x: int(regexInt.search(x.text)[0]),bandLinks))
bandName = re.search(r'([a-z_]+)\.html', bandLinks[bandCounts.index(max(bandCounts))].get("href"))[1]
print(bandName)
'''
it=1
songLinks = []
while(True):
    driver.get("http://www.tekstowo.pl/piosenki_artysty,%s,strona,%d.html"% (bandName,it))
    soup = BeautifulSoup(driver.page_source, "html.parser")
    break
'''
    #req = requests.get("http://www.tekstowo.pl/piosenki_artysty,%s,strona,%d.html"% (bandName,it))
    #soup = BeautifulSoup(req.text, "html.parser")
    it += 1
    arr = list(filter(lambda x: x.get("href").startswith("/piosenka,christina_aguilera,"), soup.find_all('a')))
    if(len(arr)==0):
        break
    songLinks += arr
songLinksLen = len(songLinks)
print("songLinksLen=%s"%(songLinksLen))
metricsFile = open('%sMetrics.txt'%(bandName),'w',encoding='utf-8')
lyricsFile = open('%sLyrics.txt'%(bandName),'w',encoding='utf-8')
it = 0
times = []
for songLink in songLinks:
    start = time.time()
    lyrics = ''
    tmpDict = {}
    
    try:
        driver.get("http://www.tekstowo.pl%s" % (songLink.get("href")))
        soup= BeautifulSoup(driver.page_source, "html.parser")

        lyrics = soup.find('div', class_='song-text').get_text().strip()
        lyrics = re.sub('\s+', ' ', lyrics)
        lyrics = re.search(r"Tekst piosenki: (.*) Poznaj histori", lyrics, re.MULTILINE)[1]
        lyrics = re.sub('\[.+?\]', '', lyrics)    
        

        tmpDict['Tytuł'] = [songLink.get_text().split('-')[1].strip()]

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
    except:
        pass
        
    lyricsFile.write(lyrics+'\n')
    metricsFile.write(str(tmpDict)+'\n')
    it += 1
    times.append(time.time()-start)
    print('%d/%d Estimated time : %f s'%(it,songLinksLen,(sum(times)/len(times))*(songLinksLen-it)))
    #if(tmpDict['Wykonanie oryginalne']==["Christina Aguilera"]):
    #    break    
driver.quit()
metricsFile.close()
lyricsFile.close()
"""
for songLink in songLinks:    
    driver.get("http://www.tekstowo.pl%s" % (songLink.get("href")))
    soup = BeautifulSoup(driver.page_source, "html.parser")  
    text = soup.find('div', class_='song-text').get_text().strip()
    text = re.sub('\s+', ' ', text)
    text = re.search(r"Tekst piosenki: (.*) Poznaj histori",text, re.MULTILINE)[1]
    print(text)
    break
driver.quit()
"""
'''
