all: clean run

clean:
	@echo "Cleaning data..."
	rm -f data/*.json
	@echo "Cleaning data finished"

run:
	@echo "Running script..."
	python3 src/Script.py
	@echo "Running script done"

# build tidak dibutuhkan karena menggunakan interpter (python)