from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import json

#open file
filename = "data/result.json"
f = open(filename,"w")

#initialize json data
data = {"jobs":[]}

#get last page
url = "https://www.jobs.id/lowongan-kerja?halaman=1"
uClient = uReq(url)
page_base = uClient.read()
uClient.close()
page_soup = soup(page_base, "html.parser")
last_page_container = page_soup.findAll("li",{})
last_page = last_page_container[8].a["href"].split("=")
last_page = int(last_page[1])

#grabs jobs from page 1 to last page
for i in range(1,last_page+1):
	#page's i url
	url = "https://www.jobs.id/lowongan-kerja?halaman=" + str(i)

	#open connection
	uClient = uReq(url)
	page_base = uClient.read()
	uClient.close()

	#html parsing
	page_soup = soup(page_base, "html.parser")

	#grabs jobs
	containers = page_soup.findAll("div",{"class":"single-job-ads"})

	#grab each job datum in a page
	for container in containers:
		stuff = container.div

		stuff = stuff.findAll("div",{"class":"col-xs-8"})
		job_title = stuff[0].h3.text.strip()

		stuff = stuff[0].findAll("p",{})
		comp_loc = stuff[0].text.split('\n')
		company = comp_loc[1]
		location = comp_loc[4]

		salary_container = stuff[1].findAll("span",{})
		if len(salary_container)>1:
			salary = salary_container[0].text.strip() + " "
			salary = salary + salary_container[1].text.strip() + " - "
			salary = salary + salary_container[2].text.strip()
		else:
			salary = salary_container[0].text.strip()

		upload_date = stuff[3].text.strip()
		stuff1 = stuff[2].text.strip()
		stuff1 = stuff1.split('\n')
		for j in range(0,len(stuff1)-1):
			if j==0:
				short_description = stuff1[j].strip()
				continue
			short_description = short_description + ". " + stuff1[j].strip()

		datum = {
			"job_title": job_title,
			"company": company,
			"location": location,
			"salary": salary,
			"upload_date": upload_date,
			"short_description": short_description
			}
		
		data["jobs"].append(datum)
	
	print("Page " + str(i) + " done.")

json.dump(data,f,indent=2)

f.close()