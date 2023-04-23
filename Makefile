

encode:
	python3 ecc.py -e example.txt output.txt

decode:
	python3 ecc.py -d bad.txt.txt fixed.txt
	cmp example.txt fixed.txt

distort:
	convert -rotate 0.5 data.png data.png

ocr:
	tesseract data.png bad.txt
