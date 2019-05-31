all: clean run

clean:
	@echo "Cleaning data..."
	del /f data\*.json
	@echo "Cleaning data finished"

run:
	@echo "Running script..."
	py src/Script.py
	@echo "Running script done"

# build tidak dibutuhkan karena menggunakan interpter (python)