#ifndef GRAPH_H
#define GRAPH_h

typedef struct {
	int v; //Vertice inicial
	int w; //Vertice final 
    float peso; //Peso del arco
} Edge;

typedef struct {
    int num ;
    char *pag;
    char *web;
    float peso;  
	int visited; // O o 1
} Nodo ;


struct graph{
	int N; //Numero de vertices
	int A; //Numero de arcos
	Edge *edges; //Arreglo de arcos
	Nodo *nodos; //Arreglo de Nodos

};

typedef struct graph *Graph;

Graph createGraph(int N);
Edge createEdge(int v, int w, float peso);
Nodo createNodo( int num, char *pag, char *web, float peso);
void insertNodo(Graph G, Nodo V, int pos);
void insertEdge(Graph G, Edge E);
void freeGraph(Graph G);
float probCalculator(Graph G, int init, int end);



#endif