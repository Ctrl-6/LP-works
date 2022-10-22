#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "graph.h"


int main(int argc, char *argv[]){

    FILE *file = fopen ( argv[1] , "r" );
	if (file == NULL ) {fputs ("File error\n",stderr); exit (1);}
    
	int init = -1, end = -1;
	float prob;
	

    int N ;
    fscanf(file,"%d\n", &N); 
    
	Graph G = createGraph(N); // Crear Grafo G
	
	
	// Sacar informacion del archivo.

	for(int i = 0 ; i < G->N ; i++){
		char *name = (char*)malloc(sizeof(char)*13) ; 
		char *web = (char*)malloc(sizeof(char)*13);
    	int  n_vecinos, vecino;
    	float peso, p_arco;
		
		fscanf(file,"%s %s %f %d\n", name, web, &peso, &n_vecinos); 
   		insertNodo(G , createNodo(i, name, web, peso), i);
		for (int j = 0 ; j < n_vecinos ; j++){
            fscanf(file,"%d %f\n" , &vecino, &p_arco);
			insertEdge(G, createEdge(i, vecino, p_arco));
		}
	}
	
	fclose (file);
	
	//imprimir por pantalla
	for(int i = 0; i < G->N ; i++){
		printf("nombre: : %s\n", G->nodos[i].pag);
		printf("web: : %s\n", G->nodos[i].web);
		for (int j = 0 ; j < G->A  ; j++){
			if (G->edges[j].v == G->nodos[i].num)
				printf("--> %s\n", G->nodos[G->edges[j].w].pag );
		}
		printf("\n");
	}
	
	for(int i = 0; i < G->N ; i++){
		if (strcmp(G->nodos[i].pag, argv[2]) == 0)
			init = G->nodos[i].num;
		if (strcmp(G->nodos[i].pag, argv[3]) == 0)
			end = G->nodos[i].num;
	
	}
	
	if (init == -1 || end == -1){
		if (init == -1) printf("El sitio %s no esta en el archivo\n", argv[2]);
		if (end == -1) printf("El sitio %s no esta en el archivo\n", argv[3]);
		printf("Imposible calcular probabilidad\n"); 
		freeGraph(G);  
		return 0;
	}
	
	prob = 100 * probCalculator(G, init, end);
	printf("La probabilidad de visitar %s iniciando la navegacion en %s, es igual a %f porciento.\n", argv[3], argv[2], prob);

	
	
	freeGraph(G);    
    return 0;
}
