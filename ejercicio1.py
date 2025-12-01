vocales=['a','e','i','o','u']
lista=[]
largas=""
pares=""
corta=""
especial=""
repetidas=""

salir=False
while not salir:
    palabras = input("ingrese alguna palabra")
    for palabra in palabras:
        if len(palabra) >= 5:
            lista = {
                "larga": palabras,
            }
        else:
            lista = {
                "cortas": palabras,
            }
        if palabra in vocales:
            lista = {
                "escpeciales": palabras,
            }
        if len(palabra) % 2 == 0:
            lista = {
                "pares": palabras,
            }
    if palabras== "salir":
        salir=True

for i in lista:
    print(i)



