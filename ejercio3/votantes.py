import socket as sk
from copyreg import pickle


sock=sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
puerto=23000
salir=False
while not salir:
    voto={int(input("voto:"))}
    sock.sendto((pickle.dumps(voto)),("127.0.0.1", puerto))
    print("voto",voto)
    if voto=="salir":
        salir=True

#me olvide la sintaxis de pickle