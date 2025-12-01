martiz = [
    {"areas":"a1"}, {"areas":"a2"}, {"areas":"a3"},
    {"areas":"b1"}, {"areas":"b2"}, {"areas":"b3"},
    {"areas":"c2"}, {"areas":"c3"}, {"areas":"c4"}
      ]


def pintarMartiz(area,reforestado):
    if area == martiz["areas"]:
        nombrearea=input("nombre area")
        martiz.append({"area": nombrearea, "reforestado":reforestado})


def reforestar(area):
    for i in martiz:
        if i["area"] == area:
            return i["reforestado"][True]
def nuevoCampo(area,planta):
    permitidos=["pino","encima","haya","roble","matorral"]
    if area == martiz["areas"] and planta in permitidos:
        nuevo = {"tipoPrincipal":f"{planta}"}
        martiz.append(nuevo)
def losreforestados():
    for i in martiz:
        if i["reforestado"] == True:
            return i["reforestado"]



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

