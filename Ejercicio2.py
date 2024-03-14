#Ejercicio 2: Un nombre propio debe escribirse con la primera letra en mayúscula. Diseña instrucciones para 
#corregirlo en caso de que esté escrito con una letra minúscula.

def corregir (nombre):
    #miramos si la primera es minuscula
    if nombre and nombre[0].islower():
        correccion = nombre.capitalize()
        return correccion
    else:
        return nombre

#ejemplo
nombre= "sara"

print("Nombre corregido:", corregir(nombre))