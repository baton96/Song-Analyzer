from concurrent.futures import ThreadPoolExecutor
from aiohttp import ClientSession
from bs4 import BeautifulSoup
from asyncio import gather
from time import time
from os import remove
from re import sub

artist = 'billie_eilish'
#buf = open('buf', 'w', encoding="utf-8")
songsFile = open(f'{artist}.txt', 'w', encoding="utf-8")

def processLine(line):
    lyrics = BeautifulSoup(line, "html.parser")
    lyrics = lyrics.find('div', class_='song-text').get_text()
    lyrics = lyrics.replace('Tekst piosenki:','')
    lyrics = sub('Poznaj histori.*', '', lyrics)
    lyrics = sub('\[.*?\]', '', lyrics)
    lyrics = sub("\'.*? ", ' ', lyrics)
    lyrics = sub('[^a-zA-Z\s]', '', lyrics)
    lyrics = lyrics.strip()
    lyrics = sub('\s+', ' ', lyrics)        
    lyrics = lyrics.lower()    
    songsFile.write(lyrics+'\n')
  
async def fetch(url, session):
    async with session.get(url) as resp:
        buf.write(re.sub('\s+', ' ', await resp.text())+'\n')
    
async def fetchAll(urls):
    async with ClientSession() as session:
       await gather(*[fetch('https://www.tekstowo.pl'+url, session) for url in urls])
'''
page = f'/piosenki_artysty,{artist}.html'
allLinks = []
lastSong = ''
while True:
    soup = BeautifulSoup(requests.get('https://www.tekstowo.pl'+page).content.decode('utf-8'), "html.parser")
    allSongs = [song for song in soup.find('div', class_='ranking-lista').findAll('a', class_='title')]
    for song in allSongs:
        songName = re.sub(' \(.*?\)', '', song['title'])
        if songName!=lastSong:
            allLinks += [song['href']]
        lastSong = songName
    nextPage = soup.find('a', {'title':'Następna >>'})
    if nextPage!=None:
        page = nextPage['href']
    else:
        break

loop = asyncio.get_event_loop()
loop.run_until_complete(fetchAll(allLinks))
buf.close()
'''
buf = open('buf.txt', 'r', encoding="utf-8")
start = time()
with ThreadPoolExecutor() as executor:
    executor.map(processLine, (line for line in buf))
print(time()-start)
buf.close()
songsFile.close()
#os.remove("buf")
