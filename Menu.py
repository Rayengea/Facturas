from test3 import cabecera # para la cabecera 
from tabulate import tabulate # para imprimir tabla
from remov import rem # importamos la def2 para tabla
from pyfiglet import figlet_format # PARA IMPRIMIR  FACTURAS 

def menu():
    print(figlet_format("FACTURA",font="slant")) #  ASCCI  DIBUJO 
    ret= '''    1)Visualisar facturas
    2)Borar facturas
    3)Dar de alta factura
    0)Salir '''
    return ret 

while True:
  print(menu())
# Se pregunta que accion se desea ejecutar 
  x=input("¿Que desea hacer?")

# Si se a elegido la opccion 1
  if x=="1":
    inp1='''¿Como desea visualizar la factura?
        a)Por pantalla desde el disco
        b)Por memoria'''
    print(inp1)
    aob=input("¿Que desea hacer?")
    if aob=="a" :
        print("FUNCION QUE ABRE UN FICHERO JSON ")
    if aob=="b" :
        print("OTRA FUNCION NO ENTEINDO ESA PARTE")

# Si se a elegido la opccion 2
  if x=="2":
    rem()

# Si se a elegido la opccion 3
  if x=="3":
    inp2='''Puedes hacer las siguientes acciones 
        a)Cabecera y detalle '''
    print(inp2)
    aob=input("Que accion deseas elegir?")
    if aob=="a" :
        cabecera()

# Si se a elegido la opccion 0
  if x=="0":
    break

