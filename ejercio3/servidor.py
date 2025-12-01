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

    print(f"binevenido ip {registrado} ")
    print(f"direcioIp={direccion[0]}-puerto{direccion[1]}-voto{datos.decode()}")


