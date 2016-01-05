CC=gcc
CFAGS=-g -Wall

all: slice_parce comp

slice_parce: slice_parce.c 
	$(CC) $(CFAGS) slice_parce.c -o slice_parce

comp: comp.c
	$(CC) $(CFAGS) comp.c -o comp

clean:
	rm slice_parce comp

