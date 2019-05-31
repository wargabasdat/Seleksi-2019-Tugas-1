all: clean build run

clean: rm data/data*

build: # compile to binary (using interpreter, not implementing)

run: python3 src/Scrap.py Comedy #genre could be change as preferences