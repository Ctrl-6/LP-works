#include <stdlib.h>
#include "graph.h"

//Crear Grafo Vacio
Graph createGraph(int N){
    Graph G = (Graph)malloc(sizeof(*G)); //Cabecera del grafo 
	G->N = N; G->A = 0; //con N nodos y 0 enlaces
	G->nodos = (Nodo*)malloc(N * sizeof(Nodo)); 
	G->edges  = NULL;
	return G;
}

//Crear Arco
Edge createEdge(int v, int w, float peso){
    Edge E;
	E.v = v;
	E.w = w;
	E.peso = peso;
	return E;
}

//Crear Nodo
Nodo createNodo( int num, char *pag, char *web, float peso) {
	Nodo V;
	V.num = num;
	V.pag = pag;
	V.web = web;
	V.peso = peso;
	return V;
}

//Insertar Nodo en Grafo
void insertNodo(Graph G, Nodo V, int pos){
	G->nodos[pos].num = V.num;
	G->nodos[pos].pag = V.pag;
	G->nodos[pos].peso = V.peso;
	G->nodos[pos].web = V.web;
}

//Insertar Arco en Grafo
void insertEdge(Graph G, Edge E){
	G->A++;
	G->edges = (Edge*)realloc(G->edges, (G->A)*sizeof(Edge)); //Reajustar tamaño de arreglos de arcos
	G->edges[G->A - 1] = E; //Agregar arco al final del arreglo
}


//Liberar memoria
void freeGraph(Graph G){
    free(G->nodos); //Lista de nodos
	free(G->edges); //Lista de arcos
	free(G);	//Finalmente la cabecera
}

float probCalculator(Graph G, int init, int end){
	if (init == end)
		return 1.0;
	float prob = 0;
	G->nodos[init].visited = 1;
	for(int i = 0; i < G->A ; i++){
		if(G->edges[i].v == init && G->nodos[G->edges[i].w].visited == 0){
			prob = prob + G->edges[i].peso * G->nodos[init].peso * probCalculator(G, G->edges[i].w, end);
		}
	}
	
	G->nodos[init].visited = 0;
	return prob;









}