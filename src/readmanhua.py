import json
import time
import requests
import re
from bs4 import BeautifulSoup

def getRequest(url):
	header = {'user-agent':'GoogleChrome (Windows x8664); Desya Anugrah/13517037@stei.itb.ac.id'}
	page = requests.get(url, headers= header).text
	soup = BeautifulSoup(page, "html.parser")
	time.sleep(1)
	return soup

def getData(url, soup):
	global record
	extracted_record = []
	daftar = soup.findAll("div", {"class":"page-item-detail manga"})
	for data in daftar:
		url_manga = data.div.a["href"]
		judul = data.div.a["title"]
		record = {
			'Title' : judul,
			'Url' : url_manga,
			'Summary' : None,
			'rateData' : None,
			'rankData' : None,
			'Author' : None,
			'Artist' : None,
			'Genres' : None,
			'Status' : None,
			'Release' : None
		}
		getDataDetail(url_manga, getRequest(url_manga))
		extracted_record.append(record)
	return extracted_record
		#print(record)


def getDataDetail(url, soup):
	global record

	summary = soup.find("div", {"class":"summary__content"}).text.strip()
	record['Summary'] = summary

	post_content = soup.findAll("div", {"class":"post-content_item"})
	#extract rate
	rate_data = post_content[0].find("div", {"class":"summary-content vote-details"}).text
	listRate = (re.findall('\d+', rate_data))
	rating = float(listRate[0]+'.'+listRate[1])
	vote = int(listRate[3])
	rateData ={
		'Rating' : rating,
		'Vote' : vote
	}
	record['rateData'] = rateData
	
	#extract rank
	rank_data = post_content[1].find("div", {"class":"summary-content"}).text
	listRank = (re.findall('\d+', rank_data))
	ranking = int(listRank[0])
	views = int(listRank[1])
	rankData ={
		'Ranking' : ranking,
		'Views' : views
	}
	record['rankData'] = rankData

	author = post_content[3].find("div", {"class":"author-content"}).text.strip()
	record['Author'] =  author

	artist = post_content[4].find("div", {"class":"artist-content"}).text.strip()
	record['Artist'] = artist

	#extract genres
	genres = []
	genreData = post_content[5].find("div",{"class":"genres-content"}).findAll("a")
	for genre in genreData:
		genres.append(genre.text)
	record['Genres'] = genres

	status = post_content[8].find("div", {"class":"summary-content"}).text.strip()
	record['Status'] = status

	#extract chapter
	chapters = soup.findAll("li",{"class":"wp-manga-chapter"})
	releaseData = []
	for chapterData in chapters:
		chapter = (re.findall('\d+', chapterData.a.text))[0]
		release_date = chapterData.span.text.strip()
		url_chapter = chapterData.a['href']
		release = {
			'Chapter' : chapter,
			'Release Date' : release_date,
			'Url Chapter' : url_chapter
		}
		releaseData.append(release)
	record['Release'] = releaseData

###MAIN##
if __name__ == "__main__":
	url = 'https://readmanhua.net/'
	with open('data.json', 'w') as outfile:
		json.dump(getData(url,getRequest(url)), outfile, indent = 4)