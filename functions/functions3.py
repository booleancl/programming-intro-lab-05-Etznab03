# Funciones con parametros
def print_param(daddy):
    print(daddy)
    print(daddy)

print_param(77)   

# no es necesario que el nombre del objeto que vamos a pasar como argumento sea el mismo que el nombre del parametro

singer = "Marcianeke"
print_param(singer)

#volumen de esfera que recibe un parametro que es
#formula 4/3pir3
def volumen(radio):
   result = 4/3 * 3.1416 * radio ** 3
   print(result)

big = 7
small = 2
volumen(big)
volumen(small)

def multiply_by_2_(number):
    number = number * 2
    print(number)

multiply_by_2_(big)
print(big)

def concat_strings(strl,str2):
    longstr = strl + " " + str2
    print(longstr)

text1 = "hola"    
text2 = "hola2"
concat_strings(text1,text2)
