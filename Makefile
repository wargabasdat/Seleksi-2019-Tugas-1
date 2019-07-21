all: clean run

clean: 
	del data\data.json

run: 
	python src/penayangan_film.py