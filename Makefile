PROJ_NAME  =  Conlangs de Burke

#################################################
#
#  Build controllers
#
#################################################

TEXER      = luatex

#################################################
#
#  Targets
#
#################################################

.PHONY: default
default: build

build:

compile:
	$(TEX) 

clean:
	rm -f *.aux *.lof *.log *.out *.toc

full-clean:
	make clean
	rm -f *.pdf
