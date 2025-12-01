import socket as sk
sock=sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
puerto=23000
salir=False
while not salir:
    voto=int(input("enviar voto"))
    sock.sendto(str(voto).encode(),("127.0.0.1",puerto))
    print("voto",voto)
    if voto=="salir":
        salir=True