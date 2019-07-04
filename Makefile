all : clean run

clean : 
	rm data/data.json

run:
	python src/dataScrapping.py