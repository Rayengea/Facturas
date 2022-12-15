from pyfiglet import figlet_format #importes 
import os  
def rem():
    #Informacion 
    Informacion='''
    --SI BORRA EL FICHERO NO PODRA RECUPERARLO-- 
    '''
    print(Informacion)
    
    fich=os.listdir("FACTURAS") # Se encarga de recorrer todos los ficheros de la carpeta
    # Recorre los archivos de esa carpeta ya que todas las facturas se guardaran en la misma
    l=[]
    for i in fich:
        l.append(i)
    x=1
    # Para añadir ficheros a la lista 
    
    for i in range(1, len(l)+1): #Esto hara que la primera opcion no sea la 0, si no la 1
        print("{}){}".format(x,l[i-1])) # x es el enumerador y 
        x=x+1
    
    inp=int(input("Que fichero deseas boras"))
    if inp in range(1, len(l)+1): # como se empieza en 1 tenemos que anadir al len +1 ya que si no se va omitir un valor 
           os.remove("FACTURAS\{}".format(l[inp-1])) #  aqui tenemos que quitar  uno ya que como en la lista se empieza desde 0 
           print(figlet_format("succes",font="slant")) # ASCII PINT
    else:
        print(figlet_format("404",font="slant"))   #ASCII imprime ERRROR 



        
    
            