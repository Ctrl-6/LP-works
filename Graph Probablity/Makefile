all: rec

rec: main.o graph.c
	gcc -Wall -o rec main.o graph.c -o tarea-2

main.o: main.c graph.h
	gcc -Wall -c main.c

clean:
	rm *.o *~ rec
