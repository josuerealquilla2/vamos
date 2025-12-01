vocales=['a','e','i','o','u']
lista=[]
salir=False
while not salir:
    palabras = input("ingrese alguna palabra o salir")
    for palabra in palabras:
        if len(palabra) >= 5:
            lista.append( {
                "larga": palabras,
            })
        else:
            lista.append({
                "cortas": palabras,
            })
        if palabra in vocales:
            lista.append({
                "especiales": palabras,
            })

        if len(palabra) % 2 == 0:
            lista.append({
                "pares": palabras,
            })
    if palabras== "salir":
        salir=True




