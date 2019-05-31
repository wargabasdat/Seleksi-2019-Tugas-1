all: clean build run

clean: # remove data and binary folder
	rm -Rf data\top_books_${genre}.csv
	
build: #not implemented as python is an intrepreted language?

run: # run your binary
	scrapy runspider src/GR_TopBooks_Spider.py -a username=${username} -a password=${password} -a genre=${genre} -a intial_page_num=${init_pnum} -a last_page_num=${last_pnum}
	python src/data_organizer.py ${genre}