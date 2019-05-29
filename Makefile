all: clean run

clean: 
	find . -name "data" -exec rm -rf {} +

run:
	python3 ./src/scrape.py