all: clean build run

clean: # remove data and binary folder
	rm data/*
	rm -rf src/__pycache__

build: # compile to binary (if you use interpreter, then do not implement it)

run: # run your binary
	python3 src/main.py
