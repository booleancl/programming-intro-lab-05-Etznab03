# Nuestra primera funcion
def songs():
    print("No te pares frente a mi")
    print("Con esa mirada tan hiriente")
    
songs()
print(type(songs))

#Las funciones se pueden usar también dentro de otras funciones
def chorus():
    songs()
    songs()

chorus()    