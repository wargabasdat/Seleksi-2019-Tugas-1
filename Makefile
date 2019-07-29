all: clean build run

clean: mvn clean # remove target/goal folder

build: mvn package # add target/goal folder

run: mvn exec:java -DHttpRequest -Dexec.args="https://www.kompas.com/" # create json file from get request of www.kompas.com