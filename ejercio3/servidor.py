import socket as sk
sock=sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
puerto=23000
sock.bind(("127.0.0.1",puerto))
registro={}
historial=[]

while True:
    datos,direccion=sock.recvfrom(1024)
    if direccion not in registro:
        nuevo=registro[direccion]
        registro[direccion]=nuevo
    registrado=registro[direccion]

    if datos == int:
        historial.append(datos)
    media=sum(historial)/len(historial)
    totaldeVotos=len(historial)
    if datos == str:
        print("no puedes enviar esto solo numeros")


    print(f"binevenido ip {registrado} ")
    print(f"direcioIp={direccion[0]}-puerto{direccion[1]}-voto{datos.decode()} ")
    print(f"media={media}")
    print(f"totaldeVotos={totaldeVotos}")


