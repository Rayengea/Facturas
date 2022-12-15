from pyfiglet import figlet_format #importes 
import os  
def eliminar():
    #Info
    Informacion='''
    --SI BORRA EL FICHERO NO PODRA RECUPERARLO-- 
    '''
    print(Informacion)
    
    fich=os.listdir("FACTURAS") # Se encarga de recorrer todos los ficheros de la carpeta

    # Añade todos los ficheros a la lista 
    l=[]
    for i in fich:
        l.append(i)
    x=1
    
    for i in range(1, len(l)+1): #Esto hara que la primera opcion no sea la 0, si no la 1
        print("{}){}".format(x,l[i-1])) # Imprime los archivos de forma que se empiece desde 1
        x=x+1
    
    inp=int(input("¿Que fichero deseas borrar?"))
    if inp in range(1, len(l)+1): # como se empieza en 1 tenemos que anadir al len +1 ya que si no se va omitir un valor 
           os.remove("FACTURAS\{}".format(l[inp-1])) #  aqui restamos 1 para que se borre el archivo correcto 
           print(figlet_format("Borrada",font="slant")) # Imprime Borrada
    else:
        print(figlet_format("ERROR",font="slant"))   #Imprime ERROR 


        
    
            