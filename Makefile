all: clean run

clean:
    find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +

run:
	python3 src/main.py
