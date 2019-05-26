''' NIM/Nama  : 13517137/Vincent Budianto
	Nama file : scrape.py
	Topik     : Data Scraping
	Tanggal   : 31 Mei 2019
	Deskripsi : Program untuk melakukan data scraping dari kulineran.com '''

#Library
import bs4
import json
import copy
import os
import re
import requests
import time

#Inisialisasi Variabel Global
global header
global restaurant_link
global result

#Inisialisasi Variabel
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
email = '13517137@std.stei.itb.ac.id'
header = {'user-agent' : useragent, 'from': email}
restaurant_link = []
result = []

#Fungsi dan Prosedur
#Prosedur untuk melakukan data scraping untuk mendapatkan semua link restoran dari list restoran kulineran.com
def scrape_kulineran():
	global header
	global restaurant_link

	for i in range(1, 8):
		url = 'https://kulineran.com/?action=restoran.list&page=' + str(i)
		request = requests.get(url, headers = header, timeout = 5)
		soup = bs4.BeautifulSoup(request.text, 'html.parser')
		restaurant_list = soup.find_all('a', href = True)

		for j in restaurant_list:
			link = str(j['href'])
			
			if ((link.startswith('//kulineran.com/restoran')) and not(link.endswith('.html')) and not('area' in link) and not('jenis' in link)  and not('jual' in link)  and not('list' in link)):
				if link not in restaurant_link:
					restaurant_link.append(link)

		time.sleep(2)
	
	restaurant_link.sort()
	get_result()

#Prosedur untuk menyimpan hasil data scraping setiap restoran
def get_result():
	global restaurant_link
	global result

	for link in restaurant_link:
		restaurant_url = 'https:' + link
		temp = get_data(restaurant_url)
		print(temp)
		result.append(temp)
		time.sleep(2)

#Fungsi untuk mengembalikan hasil data scraping setiap restoran
def get_data(url):
	global header

	request = requests.get(url, headers = header)
	soup = bs4.BeautifulSoup(request.content.decode('utf-8', 'ignore').replace('\u200b', ''), 'html.parser')
	info = soup.find(attrs = {'class': 'gerai-info'}).find_all('li')
	category = info[0].text.split(", ")
	name = soup.find(attrs = {'class': 'gerai-name'}).get_text(strip = True)

	if (('TUTUP' in name) or ('LIBUR' in name)):
		name = name[:-5]

	address = info[1].get_text(strip = True)[8:]
	phone = re.sub('[^0123456789/]', '', (info[2].get_text(strip = True)[7:].replace(',', '/'))).split('/')
	
	for i in range(len(phone)):
		if (len(phone[i]) < 6):
			del phone[i]

	likes = soup.find(attrs = {'class': 'like'}).get_text(strip = True)
	dislikes = soup.find(attrs = {'class': 'dislike'}).get_text(strip = True)
	logo = soup.find(attrs = {'class': 'gerai-logo'}).find('img')['src']
	menu = []
	menu_list = soup.find(attrs = {'class': 'menu-list'}).find_all('tr')

	if menu_list is None:
		menu.append('N/A')
	else:
		for j in range(len(menu_list)):
			if (menu_list[j].find('td')):
				item = menu_list[j].get_text(strip = True).split('Rp ')

				if (menu_list[j].find('br')):
					if (len(item) < 2):
						price = '-'
					else:
						price = item[1]
					
					food = [menu_list[j]['id'], menu_list[j].find('br').previous_sibling.replace('\t', '').replace('\n', ''), price, re.sub('[(){}]', '', (menu_list[j].find('br').next_sibling.get_text(strip = True)))]
				else:
					if (len(item) < 2):
						item.append('-')
					
					food = [menu_list[j]['id']] + item + ['-']
			
				menu.append(food)

	menu.sort()
	photo = []
	photo_list = soup.find(attrs = {'class': 'gerai-images'}).find_all('img', attrs = {'u': 'image'})

	if photo_list is None:
		photo.append('N/A')
	else:
		for k in range(len(photo_list)):
			photo.append(photo_list[k]['src'])

	return [category, name, address, phone, likes, dislikes, logo, menu, photo]

#Prosedur untuk menyimpan hasil data scraping ke dalam file berformat .json
def get_json():
	global result

	jdata = {}
	data = []

	for res in result:
		menu = []
		photo = []
		jdata['Category'] = res[0]
		jdata['Name'] = res[1]
		jdata['Address'] = res[2]
		jdata['Phone'] = res[3]
		jdata['Likes'] = res[4]
		jdata['Dislikes'] = res[5]
		jdata['Logo'] = res[6]
		menu_list = res[7]

		for i in range(len(menu_list)):
			menu.append({'Menu_ID': menu_list[i][0], 'Menu_Name': menu_list[i][1], 'Price': menu_list[i][2], 'Description': menu_list[i][3]})

		jdata['Menu'] = menu
		photo_list = res[8]

		for j in range(len(photo_list)):
			photo.append({'Photo_Link': photo_list[j]})

		jdata['Photos'] = photo
		data.append(copy.deepcopy(jdata))
	
	path = '../data/'
	filename = 'data.json'

	with open(os.path.join(path, filename), 'w', encoding = 'utf8') as fileout:
		json.dump(data, fileout, ensure_ascii = False, indent = 4)

#Main Program
if (__name__ == "__main__"):
	scrape_kulineran()
	get_json()
