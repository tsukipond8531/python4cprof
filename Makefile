.PHONY: test

BUILD := build

all: ${BUILD}/texto.pdf

${BUILD}/texto.md: texto.md bin/inclui.py src/*
	mkdir -p ${BUILD}
	./bin/inclui.py < texto.md > ${BUILD}/texto.md

${BUILD}/texto.pdf: ${BUILD}/texto.md
	mkdir -p ${BUILD}
	pandoc --pdf-engine tectonic -o $@ $<

test:
	python3 -B -m doctest src/*.py && echo OK
