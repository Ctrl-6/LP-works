import re
import sys

#Almacenamiento de informacion:
l_texto = []
d_tags = dict()
d_var = dict()

#Recibiendo texto de parametro 
texto = sys.argv[1]

#Expreciones Regulares
orden = re.compile(r'\w[A-Z]+')
tag = re.compile(r'=[\w]+=')
var = re.compile(r'[$][\w]+[$]')
cho = re.compile(r'\s[A-Z][^A-Z][\w\s]+') 

#Funciones
def posicionTag(linea,tag):
    if tag.match(linea) != None:
        x = tag.match(linea).group()
        return(x)

def hayTag(linea,tag):
    if tag.search(linea) != None:
        x = tag.search(linea).group()
        return(x)

    
def hayVar(linea,var):
    if var.search(linea) != None:
        return (var.findall(linea))
    


def hayOrden(linea,orden):
    if orden.search(linea) != None:
        x = orden.search(linea).group()
        return(x)

    
#Creacion de Lista(Procesamiento de texto):
archivo = open(texto, 'r')
for linea in archivo:
    l_texto.append(linea)
archivo.close()

#Creacion de Diccionario de posciones:
for linea in l_texto:
    if posicionTag(linea,tag) != None:
        d_tags[hayTag(linea,tag)] = l_texto.index(linea)
        
#Creacion de Diccionario de Variables
for linea in l_texto:
    if hayOrden(linea,orden) == "SET":
        llave = hayVar(linea,var)[0]
        linea = linea[var.search(linea).end()+1:len(linea)-1]
        d_var[llave] = linea     
     
def procesadorDeTexto(l_texto,d_tags,d_var,marcador):

    if marcador == "=finish=":
        l_aux = l_texto[d_tags[marcador]+1:(len(l_texto))]
    else:
        l_aux = l_texto[d_tags[marcador]+1:(len(l_texto)-1)]

    for linea in  l_aux:
            if linea != "\n":
                #Comprobando Ordenes
                if hayOrden(linea,orden) == "ASK":
                        if hayVar(linea,var) != None:
                            llave = str(input("\t"))
                            d_var[hayVar(linea,var)[0]] = llave

                if hayOrden(linea,orden) == "SET":
                    llave = hayVar(linea,var)[0]
                    frase = linea[var.search(linea).end()+1:len(linea)-1]
                    d_var[llave] = frase     
                

                if hayOrden(linea,orden) == "CHOICE":
                    tag_opc = tag.findall(linea)
                    opciones =  cho.findall(linea)
                    for i in tag_opc:
                        print("\t"+str([tag_opc.index(i)+1]) + str(opciones[tag_opc.index(i)]))           
                    eleccion = input()
                    x = tag_opc[int(eleccion)-1]
                    procesadorDeTexto(l_texto,d_tags,d_var,x) 

    
                if hayOrden(linea,orden) == "GOTO":
                    procesadorDeTexto(l_texto,d_tags,d_var,hayTag(linea,tag))
                    
                    

                #Reemplazando Variables
                if hayVar(linea,var) != None: 
                    for i in hayVar(linea,var):
                        linea = linea.replace(i,d_var[i])
                        
                    

                if hayOrden(linea,orden) == None:
                    print(linea)


            else:
                break
            
           
            

#LLamado Funcion Principal
procesadorDeTexto(l_texto,d_tags,d_var,"=start=")






















