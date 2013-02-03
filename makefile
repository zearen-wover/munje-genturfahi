all: Main

.PHONY: Main
Main:
	ghc -outputdir build --make Main.hs

.PHONY: clean
clean:
	mv build/dummy .
	rm -rf Main build/*
	mv dummy build
