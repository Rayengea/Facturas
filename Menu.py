from generador import generar # Para crear la factura.
from tabulate import tabulate # Para crear la tabla de impresion.
from eliminar import eliminar # Importamos la def2 para tabla
from pyfiglet import figlet_format # Para dibujar.
from modificar import modif #Para modificar las factuaras
from visualizar import visualizar # Para visualizar las facturas.
def menu():
    print(figlet_format("FACTURAS",font="slant")) # Crea el dibujo con la palabra "facturas"
    ret= '''    1)Visualisar facturas
    2)Borar facturas
    3)Dar de alta factura
    4)Modificar facturas
    0)Salir '''
    return ret 

while True:
  print(menu())
# Se pregunta que accion se desea ejecutar 
  x=input("¿Que desea hacer?")
# Si se a elegido la opccion 1
  if x=="1":
    try:
      inp1='''Aqui tienes las facturas:
      
      '''
      print(inp1)
      visualizar()
    except:
      print("Aun no hay facturas.")
# Si se a elegido la opccion 2
  if x=="2":
    try:
      eliminar()
    except:
      print("Aun no hay facturas.")
# Si se a elegido la opccion 3
  if x=="3":
    generar()
#Si se ha elegido la opcion 4
  if x=="4":
    modif()
# Si se a elegido la opccion 0
  if x=="0":
    print(figlet_format("Gracias y hasta pronto",font="slant"))
    break

