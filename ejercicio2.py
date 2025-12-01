martiz = [

      ]


def reforestar(area):
    for i in martiz:
        if i["area"] == area:
            return i["reforestado"][True]
def nuevoCampo(planta):
    permitidos=["pino","encima","haya","roble","matorral"]
    if planta in permitidos:
        martiz.append({
            "tipoPrincipal": planta,
        })

def pintarMartiz(area,reforestado):



print(reforestar("1b"))
for i in martiz:
    print(i)

menu = input(f"menu:\n""pintarRe = 0\nreforestar = 1\ntipoPrincipal = 2\n")
if menu == "1":
    area=  input("escriba el area: ")
    print(reforestar(area))
if menu == "2":
    plantas= input("escriba la planta: ")
    print(nuevoCampo(plantas))

   