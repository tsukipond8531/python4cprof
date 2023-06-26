.PHONY: test

BUILD := build

all: ${BUILD}/texto.pdf

${BUILD}/%.pdf: %.md
	mkdir -p ${BUILD}
	pandoc --pdf-engine tectonic -o $@ $<

test:
	python -m doctest src/*.py && echo OK
