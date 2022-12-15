import pandas as pandas
from copy import copy 
import os 
import tabulate
def visualisar():
    fich=os.listdir("FACTURAS")
    l=[]
    for i in fich:
        l.append(i)
    x=1
    for i in range(1, len(l)+1): #Cambiamos el primer argumento que es 0 por 1
        print("{}){}".format(x,l[i-1])) #Imprime los ficheros mostrando el numero con el parentesis y despues el nombre
        x=x+1
    inp1=int(input("¿Que fichero desea?"))
    ruta="FACTURAS\{}".format(l[inp1-1])
    print(ruta)  
    
    dicionario_del_fichero=pandas.read_csv(ruta).to_dict() #Lee el archivo introducido y crea un diccionario con que esta en el fichero 
    
    dicfich=copy(dicfich) # Copia de diccionario
    texto1='''
    Empresa:¨{}
    Direccion:{},{},{}
    Contactos:{},{}  
    '''
    print(texto1.format(dicfich["Empresa"],dicfich["Calle"],dicfich["CP"],dicfich["Tlfno"],dicfich["Mail"]))

visualisar()

        

        

