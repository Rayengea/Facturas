import json 
import os 
from tabulate import tabulate
def visualizar():
    fich=os.listdir("FACTURAS")#lee la carpeta 
    
    l=[]
    for i in fich:
        l.append(i) #Itera sobre los ficheros y los añade a una lista
    
    x=1
    for i in range(1, len(l)+1): #Cambiamos el primer argumento que es 0 por 1
        print("{}){}".format(x,l[i-1])) #Imprime los ficheros mostrando el numero con el parentesis y despues el nombre
        x=x+1
    inp1=int(input("¿Que fichero deseas visualisar?"))  # Se pregunta el fichero que se desea ver y se resta 1 porque antes se le ha sumado 1.
    ruta="FACTURAS\{}".format(l[inp1-1])
    
    #Abre el archivo
    archivo=open(ruta, 'r')
    datos=json.load(archivo)
    
    #Se extrae la cabecera
    texto1='''
    Empresa:¨{}
    Direccion:{},{}
    Contactos:{},{}  
    '''
    print(texto1.format(datos["Empresa"],datos["Calle"],datos["CP"],datos["Tlfno"],datos["Mail"]))

    #Se extrae el cuerpo

    texto2= {
            'Cantidad':datos["Cantidad"],
            'Concepto': datos["Concepto"],
            'Importe/Unidad':datos["Importe/Unidad"],
            "Importe":datos["Importe"]
    }

    
    print(tabulate(texto2,headers=["Cantidad ", "Concepto","Importe/Unidad","Importe"]))

    #Se extraen los totales
   
    summ=datos["Importe"][0]+datos["Importe"][1]+datos["Importe"][2]

    print("Base imponible:   {}".format(summ))
    print("IVA 21%:   {}".format(summ*0.21))
    print("Total:   {}".format(summ+summ*0.21))

    archivo.close()
        


        

        

