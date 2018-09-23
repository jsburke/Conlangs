#############################
#                           #
# Project Files             #
#                           #
#############################

PROJ      = Banzonaa
SRC       = $(addsuffix .tex, $(PROJ))
PDF       = $(addsuffix .pdf, $(PROJ))

#############################
#                           #
# Build controls            #
#                           #
#############################

TEX        = lualatex
TEX_FLAGS  = 

VIEW       = evince

#############################
#                           #
# Targets                   #
#                           #
#############################

.PHONY: default
default: pdf 

.PHONY: pdf
pdf: $(PDF)

$(PDF): *.tex 
	make build
	make clean

.PHONY: show
show: $(PDF)
	$(VIEW) $(PDF) &

.PHONY: build
build: 
	$(TEX) $(TEX_FLAGS) $(SRC)

.PHONY: rebuild
rebuild:
	make full-clean
	make pdf

.PHONY: reshow
reshow: rebuild
	make show

.PHONY: clean
clean:
	rm -rf *.log *.aux *.dvi *.lof *.lot *.out *.toc

.PHONY: full-clean
full-clean: 
	make clean
	rm -rf *.pdf

