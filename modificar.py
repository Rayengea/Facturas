import os 
import json 
def modif():
    fich=os.listdir("FACTURAS")#lee la carpeta 
    
    l=[]
    for i in fich:
        l.append(i) #Itera sobre los ficheros y los añade a una lista
    
    x=1
    for i in range(1, len(l)+1): #Cambiamos el primer argumento que es 0 por 1
        print("{}){}".format(x,l[i-1])) #Imprime los ficheros mostrando el numero con el parentesis y despues el nombre
        x=x+1
    inp1=int(input("¿Que fichero deseas modificar?"))  # Se pregunta el fichero que se desea ver y se resta 1 porque antes se le ha sumado 1.
    ruta="FACTURAS\{}".format(l[inp1-1])
    #Abre el archivo en el modo lectura y escritura 
    
    archivo=open(ruta,'r+')
    # Carga el contenido del archivo a un diccionario
    contenido = json.load(archivo)
    x=input("Que valor deseas cambiar?")
    z=input("Cual es el nuevo valor de {} ?".format(x))
    print(x)
    print(z)
    contenido[x]=z
    

    json.dump(contenido, archivo)

    # Cierra el archivo
    archivo.close()

