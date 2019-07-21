all: clean build run

clean: # remove data and binary folder
	del data\data.json
	
build: # compile to binary (if you use interpreter, then do not implement it)

run: # run your binary
	python src/readmanhua.py
