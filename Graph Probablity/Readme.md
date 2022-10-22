# Tarea 2: Lenguaje de Programacion

  ## Intrucciones de Compilacion
  Se debe compilar el archivo nombrado como **main.c**, este necesita al archivo **graph.h**, que a la vez necesita **graph.c**.
  
  La carpeta cuenta con un archivo **Makefile**, que ejecuta las siguientes lineas:
  > gcc -Wall -c main.c  
  > gcc -Wall -o rec main.o graph.c -o tarea-2



  Este generará un ejecutable llamado "tarea-2".

## Supuestos o informacion relevante
En la funcion *probCalculator*, la funcion que utilizo para calcular la probabilidad, la manera que cree para ver si un nodo estaba visitado o no, fue agregar una variable al *struct nodo*, que guardara la condicion de ser visitado o no, y asi poder calcular la probabilidad sin problemas. La variable *Visitado*, obtiene un valor de 1 o 0, si fue visitada o no, respectivamente.

