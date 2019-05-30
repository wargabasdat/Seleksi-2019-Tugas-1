#Nama : Fata Nugraha
#NIM : 13517109

from bs4 import BeautifulSoup
import requests
import re
import json
import copy
import os

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
header = {'user-agent' : user_agent, 'email' : "13517109@std.stei.itb.ac.id"}
main_url = 'http://sbmptn.ltmpt.ac.id/?mid=14'
jsonData = {}
allData = []

mainResponse = requests.get(main_url, headers = header, timeout = 5)
mainContent = BeautifulSoup(mainResponse.content, "html.parser")


#get link to university data from the main link
univLinks = []
for link in mainContent.findAll('a', attrs={'href': re.compile("^index.php")}):
	univLinks.append('http://sbmptn.ltmpt.ac.id/' + link.get('href'))


#get link to each 'study program' data from each university link
univProdiLinks = []
for univLink in univLinks:
	univResponse = requests.get(univLink, headers = header, timeout = 5)
	univContent = BeautifulSoup(univResponse.content, "html.parser")
	for prodiSubLink in univContent.findAll('a', attrs={'href': re.compile("^index.php")}):
		univProdiLink = 'http://sbmptn.ltmpt.ac.id/' + prodiSubLink.get('href')
		if univProdiLink not in univLinks and 'ptn=999' not in univProdiLink:
			univProdiLinks.append(univProdiLink)


#get data from each 'study program' links
tempCode = ''
for univProdiLink in univProdiLinks:
	univProdiResponse = requests.get(univProdiLink, headers = header, timeout = 5)
	univProdiContent = BeautifulSoup(univProdiResponse.content, "html.parser")
	univName = univProdiContent.findAll('a', attrs={'class': re.compile("^panel-title")})[0].text
	univProdiName = univProdiContent.findAll("span", attrs={'class': re.compile("^label-success")})[0].text
	univProdiData = univProdiContent.findAll("td")
	i = 0
	while univName not in univProdiData[i].text.strip():
		i+=1
	univCode = univProdiData[i-1].text.strip()
	while 'Daya Tampung' not in univProdiData[i].text.strip():
		i+=1
	univProdiCode = univProdiData[i-3].text.strip()
	univProdiCapacity = univProdiData[i+1].text.strip()
	univProdiApplicant = univProdiData[i+7].text.strip()
	if univCode != tempCode:
		if tempCode != '':
			jsonData['Daftar Prodi'] = prodiList
			allData.append(copy.deepcopy(jsonData))
		tempCode = univCode
		jsonData['Kode Universitas'] = univCode
		jsonData['Nama Universitas'] = univName
		prodiList = []
	prodi = {}
	prodi['Kode Prodi'] = univProdiCode
	prodi['Nama Prodi'] = univProdiName
	prodi['Kapasitas'] = univProdiCapacity
	prodi['Total Peminat'] = univProdiApplicant
	detailList = []
	rincian = {}
	while 'Provinsi' not in univProdiData[i].text.strip():
		i+=1
	while True:
		i+=1
		try:
			if not univProdiData[i].text.strip().isdigit() and univProdiData[i].text.strip() != '':
				if univProdiData[i+3].text.strip() != '':
					asalDaerah = univProdiData[i].text.strip()
					peminatPerDaerah = univProdiData[i+3].text.strip()
					rincian['Asal Daerah'] = asalDaerah
					rincian['Peminat'] = peminatPerDaerah
					detailList.append(copy.deepcopy(rincian))
		except Exception as e:
			break
	prodi['Rincian Peminat'] = detailList
	prodiList.append(copy.deepcopy(prodi))
jsonData['Daftar Prodi'] = prodiList
allData.append(jsonData)

#convert to json
try:
	os.makedirs("../data")	
except Exception as e:
	pass
with open("../data/data_file.json", "w") as write_file:
    json.dump(allData, write_file, indent = 4)