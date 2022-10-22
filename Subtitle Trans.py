import re
import sys

#Almacenamiento :
d_style = {}
d_sub = {}

#Contador 
id = 0

#Recibiendo texto de parametro 
ass_name = sys.argv[1]
srt_name = sys.argv[2]

#Expreciones Regulares : 
r_dialogo = re.compile(r'(Dialogue: )(\d),(\d+:\d{2}:\d{2}.\d+),(\d+:\d{2}:\d{2}.\d+),([\w\s-]+),(\w*),(\d+,\d+,\d+),(.*?),(.+)') 
r_style = re.compile(r'(^Style: )([\w\s-]+),([\w\s]+),(\d+),(&\w+),(.+)') #2
r_color = re.compile(r'(&H00)(\w{2})(\w{2})(\w{2})')
r_time = re.compile(r'(\d*):*(\d{2}):(\d{2}).(\d{3}|\d{2})?') 

#Funciones
#Comprobar si existe la condiciond del tiempo.
time = False
if len(sys.argv) == 4 :
    time = sys.argv[3]
    end = r_time.findall(time)[1]  ##Lista = (Horas, Minutos, Segundos, Milesimas)
    start = r_time.findall(time)[0] ##Lista = (Horas, Minutos, Segundos, Milesimas)
    
    #Ajustando tupla de tiempo (nn:nn:nn:nn) 
    if start[0] == "":
        start = list(start)
        start[0] = "0" 
        
    if end[0] == "":
        end = list(end)
        end[0] = "0" 
       
     
#Funcion para transformar color.
def colorTransformation(color):
     new_color = r_color.search(color).group(4) + r_color.search(color).group(3) + r_color.search(color).group(2)
     return new_color  

#Funcion para ajustar el tiempo (Resta de tiempo)
def setTime( hora , hora2):
    config = [0,0,0,0]
    for i in range(3,-1,-1) :
        resta = int(hora[i]) - int(hora2[i])
        if resta < 0 :
            config[i-1] = config[i-1] - 1  
            if i == 3:
                config[i] =  str(1000 + (resta) + config[i])
            else:
                config[i] = str(60 + resta + config[i])
            
        else : 
            config[i] = str(resta + config[i]) 
            
        #Comprobaar si tiene el formato adecuado (dd:dd:dd:ddd)
        if i == 3 :
            if len(config[i]) == 1 :
                    config[i] = config[i] + "00"
            if len(config[i]) == 2 :
                    config[i] = config[i] + "0"
        
        else :
            if len(config[i]) == 1:
                    config[i] = "0" + config[i] 
    
    return config #Lista con nuevo tiempo configurado [nn, nn, nn, nnn]

#Funcion para crear nuevo texto
def transcribirSub(srt, dicc1, dicc2):
    archivo = open(srt + ".srt", 'w')
    for numero,descripcion  in dicc1.items(): 
        #Descripcion = (Dialogo,Inicio,Final,Estilo) 
        archivo.write(numero+ "\n")
        #Escritura de tiempo en formato correcto : Inicial = Final = list(hh,mm,ss,msmsms)
        archivo.write( ":".join(descripcion[1][:3]) + "," + descripcion[1][3] + " --> " + ":".join(descripcion[2][:3]) + "," + descripcion[2][3] + "\n")
        archivo.write('<font color="#' + dicc2[descripcion[3]] +'">' + descripcion[0] + '</font>\n\n' )
    archivo.close()

#Abrir archivo
archivo = open(ass_name, 'r') 

#Recorrer Archivo
for linea in archivo:
    #Crear Diccionario Name:Color RGB
    if r_style.search(linea) : 
       d_style[r_style.search(linea).group(2)] = colorTransformation(r_style.search(linea).group(5))
    #Ver si es subtitulo
    if r_dialogo.search(linea) :
        dialogo = r_dialogo.search(linea).group(9)
        
        #Ajuste de tiempo a formato (nn:nn:nn.nnn) ----------
        inicio = r_dialogo.search(linea).group(3)
        inicio = r_time.findall(inicio)[0]      
        inicio = list(inicio)
        inicio[3] = inicio[3] + "0"
        
        final = r_dialogo.search(linea).group(4)
        final = r_time.findall(final)[0]
        final = list(final)
        final[3] = final[3] + "0"
        #-----------------------------------------------------

        estilo = r_dialogo.search(linea).group(5)

        #Acotando si existe parametro de tiempo
        if time :
            if inicio >= start and final <= end   :
                id = id + 1
                new_inicio = setTime(inicio,start)
                new_final =   setTime(final,start)
                d_sub[str(id)] = (dialogo,new_inicio, new_final , estilo) #Agregando a diccionario para escribir.
        #si no hay parametro de tiempo       
        else:
            id = id + 1
            d_sub[str(id)] = (dialogo, inicio, final, estilo) #Agregando a diccionario para escribir.

#Cerrar archivo
archivo.close()   
#Llamado a funcion para transcribir texto.
transcribirSub(srt_name,d_sub ,d_style)

print("Convirtiendo" , ass_name , "a" , srt_name)
if time :
    print("Desde", start[0], "[h]", start[1],"[m]", start[2],"[s]", start[3], "[ms]")
    print("Hasta", end[0], "[h]", end[1],"[m]", end[2],"[s]", end[3], "[ms]")

print("Proceso Finalizado")

