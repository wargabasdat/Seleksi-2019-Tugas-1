all: clean build run

clean: # remove data
    - rm -f data/*

build: # do nothing

run: # run python interpreter
    py src/main.py