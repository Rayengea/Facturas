import json
import os 
from os import path #Para trabajar con las carpetas y ficheros.
from tabulate import tabulate 
def generar(): #Se introducen los datod de la empresa.
    a=input("Introduce el nombre de la empresa: ")
    b=input("Introduce la calle donde se encuentra la empresa: ")
    c=input("Introduce el codigo postal y la provincia: ")
    d=input("Introduce el numero de contacto: ")
    e=input("introduce el gmail de la empresa: ")
    
    #Se crea el diccionario con los datos de la empresa.
    dic={ 
        "Empresa":a,
        "Calle":b,
        "CP":c,
        "Tlfno":d,
        "Mail":e,  
        }                                                      

    #Se introdicen los productos, importe de cada uno e importe total.
    valor=0
    listaP=[]
    while True:
        try:
            inp1=int(input("Introducir cantidad de producto vendido: "))
            listaP.append(inp1)
            valor=valor+1
            if valor==3:
                break
        except:
            print("Dato introducido incorrecto.")


    valor2=0
    listaC=[]
    while True:
        inp1=input("Introducir nombre del producto: ")
        listaC.append(inp1)
        valor2=valor2+1
        if valor2==3:
            break


    valor3=0
    listaI=[]
    while True:
        try:
            inp1=int(input("Introducir importe por unidad de cada producto:"))
            listaI.append(inp1)
            valor3=valor3+1
            if valor3==3:
                break
        except:
            print("Dato introducido incorecto.")

    #Saca el precio total del producto
    producto = [x*y for x,y in zip(listaP,listaI)] 

    # Se crea el diccionario con el precio final
    dict1 = {'Cantidad':listaP,
            'Concepto': listaC,
            'Importe/Unidad': listaI,
            "Importe":producto
            }
    # Se imprime la factura
    print("Empresa {} Calle {} Codigo Postal {} Telefono {} Mail".format(a,b,c,d,e))
    print(tabulate(dict1,headers=["Cantidad ", "Concepto","Importe/Unidad","Importe"]))

    total=producto[0]+producto[1]+producto[2]

    print("Base imponible:   {}".format(total))
    print("IVA 21%:   {}".format(total*0.21))
    print("Total:   {}".format(total+total*0.21))

    #Juntamos los diccionarios en uno solo.
    factura={

    }
    factura=dic|dict1 # Funcion que junta dos diccionarios

    
    if not os.path.exists('FACTURAS'): # Busca la carpeta facturas 
        os.makedirs('FACTURAS')       # En caso de que no la encuentre, la crea

    narchiv="".join("FACTURAS/{}").format("{}.json".format(a)) #Se asigna el nombre de la empresa al nombre del fichero.

    #Se guarda el archivo en la carpeta de facturas.
    f=open(narchiv,"w")
    json.dump(factura,f)
    creada='''
    ---- FACTURA CREADA ----
    '''
    print(creada)
    f.close()

