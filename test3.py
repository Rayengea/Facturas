import json
import os 
from os import path
from tabulate import tabulate
def cabecera():
    a=input("Introduce el nombre de la empresa: ")
    b=input("Introduce la calle donde se encuentra la empresa: ")
    c=input("Introduce el codigo postal y la provincia: ")
    d=input("Introduce el numero de contacto: ")
    e=input("introduce el gmail de la empresa: ")
    
    dic={
        "Empresa":a,"Calle":b,"CP":c,"Tlfno":d,"Mail":e,  
        }                                                            
    
    valor=0
    listaP=[]
    while True:
        inp1=int(input("Introduce la cantidad de prductos que se entregan:"))
        listaP.append(inp1)
        valor=valor+1
        if valor==3:
            break


    valor2=0
    listaC=[]
    while True:
        inp1=input("Introduce el nombre de los productos:")
        listaC.append(inp1)
        valor2=valor2+1
        if valor2==3:
            break


    valor3=0
    listaI=[]
    while True:
        inp1=int(input("Introduce importe por unidad de cada producto:"))
        listaI.append(inp1)
        valor3=valor3+1
        if valor3==3:
            break

    product = [x*y for x,y in zip(listaP,listaI)]

    dict1 = {'Cantidad':list(map(str, listaP)),
            'Concepto': listaC,
            'Importe/Unidad': list(map(str, listaI)), # map transforma una lista int() en str()
            "Importe":list(map(str,product))
            }
    print("Empresa {} Calle {} Codigo Postal {} Telefono {} Mail".format(a,b,c,d,e))
    print(tabulate(dict1,headers=["Cantidad ", "Concepto","Importe/Unidad","Importe"]))

    summ=product[0]+product[1]+product[2]

    print("Base imponible:   {}".format(summ))
    print("IVA 21%:   {}".format(summ*0.21))
    print("Total:   {}".format(summ+summ*0.21))
    
    factura={

    }
    factura=dic|dict1 # Funcion que junta dos diccionarios

    if not os.path.exists('FACTURAS'): # Busca la carpeta facturas 
        os.makedirs('FACTURAS')       # En caso de que no la encuentre, la crea

    narchiv="".join("FACTURAS/{}").format("{}.json".format(a))

    f=open(narchiv,"w")
    json.dump(factura,f)
    creado='''
    ----CREADO 
    '''
    print(creado)


