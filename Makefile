all: clean build run

clean: npm run clean # remove data and binary folder

build: npm install

run: npm run start