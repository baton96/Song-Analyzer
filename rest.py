'''
with open(f'{artist}.txt', 'w') as out:    
    s = BeautifulSoup(requests.get(f'https://www.tekstowo.pl/piosenki_artysty,{artist}.html').text, "html.parser")
    allA = [a['href'] for a in s.find('div', class_='ranking-lista').findAll('a', class_='title')]
    start = time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        pass
        #executor.map(foo, allA)
    print(time()-start)

async def fetch(url, session):
    #print(f'https://www.tekstowo.pl'+url['href'])
    async with session.get(f'https://www.tekstowo.pl'+url['href']) as resp:
        s = await resp.text()
async def run(urls):
    async with aiohttp.ClientSession() as session:
       await asyncio.gather(*[fetch(url, session) for url in urls])

with open(f'{artist}.txt', 'w') as out:    
    s = BeautifulSoup(requests.get(f'https://www.tekstowo.pl/piosenki_artysty,{artist}.html').text, "html.parser")
    allA = s.find('div', class_='ranking-lista').findAll('a', class_='title')
    start = time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(allA))
    loop.close()
    print(time()-start)
'''
'''
s = BeautifulSoup(requests.get(f"https://www.azlyrics.com/{artist[0]}/{artist.replace(' ','')}.html").text, "html.parser")
allA = [a['href'] for a in s.find(id="listAlbum").findAll('a')]
start = time()
for a in allA:
    #s2 = BeautifulSoup(requests.get('https://www.azlyrics.com'+a[1:]).text, "html.parser")
    print('https://www.azlyrics.com'+a[1:])
    break
print(time()-start)
'''
'''
r = requests.get('https://www.tekstowo.pl/piosenka,linkin_park,1stp_klosr.html')
soup = BeautifulSoup(r.text, "html.parser")
lyrics = soup.find('div', class_='song-text').get_text().strip()
lyrics = re.sub('\s+', ' ', lyrics)
#lyrics = re.search(r"Tekst piosenki: (.*) Poznaj histori", lyrics, re.MULTILINE)[1]
lyrics = re.sub('[^a-zA-Z\s]', '', lyrics)

results = io.open("tmp.txt", mode="w", encoding="utf-8")
results.write(lyrics)
results.close()

print(lyrics)

class PyLyrics:
	@staticmethod 
	def getTracks(album):
		url = "http://lyrics.wikia.com/api.php?action=lyrics&artist={0}&fmt=xml".format(album.artist())
		soup = BeautifulSoup(requests.get(url).text)

		for al in soup.find_all('album'):
			if al.text.lower().strip() == album.name.strip().lower():
				currentAlbum = al
				break
		songs =[Track(song.text,album,album.artist()) for song in currentAlbum.findNext('songs').findAll('item')]
		return songs

	@staticmethod
	def getLyrics(singer, song):
		#Replace spaces with _
		singer = singer.replace(' ', '_')
		song = song.replace(' ', '_')
		r = requests.get('http://lyrics.wikia.com/{0}:{1}'.format(singer,song))
		s = BeautifulSoup(r.text)
		#Get main lyrics holder
		lyrics = s.find("div",{'class':'lyricbox'})
		if lyrics is None:
			raise ValueError("Song or Singer does not exist or the API does not have Lyrics")
			return None
		#Remove Scripts
		[s.extract() for s in lyrics('script')]

		#Remove Comments
		comments = lyrics.findAll(text=lambda text:isinstance(text, Comment))
		[comment.extract() for comment in comments]

		#Remove unecessary tags
		for tag in ['div','i','b','a']:
			for match in lyrics.findAll(tag):
				match.replaceWithChildren()
		#Get output as a string and remove non unicode characters and replace <br> with newlines
		output = str(lyrics).encode('utf-8', errors='replace')[22:-6:].decode("utf-8").replace('\n','').replace('<br/>','\n')
		try:
			return output
		except:
			return output.encode('utf-8')
import pandas as pd
singer = 'Linkin Park'
lyrics_df = []
singer = singer.replace(' ', '_')

start = time()
s = BeautifulSoup(requests.get(f'https://lyrics.fandom.com/wiki/{singer}').text, "html.parser")
div = s.find('div', class_='mw-content-text')
allA = [a['href'] for ol in div.findAll('ol') for a in ol.findAll('a') if a.has_attr('href')]
print(time()-start)

start = time()
s = BeautifulSoup(requests.get(f'https://lyrics.fandom.com/wiki/Category:Songs_by_{singer}').text, "html.parser")
allA2 = [a['href'] for a in s.findAll('a', class_='category-page__member-link')]
print(time()-start)
print(set(allA2)-set(allA))
'''
