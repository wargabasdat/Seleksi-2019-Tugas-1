all: clean run

clean: rm data/data_file.json

run: python src/data_scraping.py
