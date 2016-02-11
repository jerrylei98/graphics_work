all: main.py draw.py display.py
	@echo "'make run' for .ppm in file"
	@echo "'make imgur' to upload to imgur"
run: main.py draw.py display.py
	python main.py
imgur: main.py draw.py display.py
	python main.py imgur
clean:
	rm *.ppm
	rm *~
