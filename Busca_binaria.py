import sys
import struct
from typing import final

if len(sys.argv) != 2:
    print("Uso invalido!!! \n-> USO Python3 buscaBinaria [CEP]")
    quit()
elif len(sys.argv[1]) != 8:
    print(f"Argumento [{sys.argv[1]}] Invalido!!")
    quit()

def imprimeLinha(record):
    for i in range(0, len(record) - 1):
        print(record[i].decode("latin1"))

registroCEP = struct.Struct("72s72s72s72s2s8s2s")

with open("cep_ordenado.dat", "rb") as arq: 
    arq.seek(0,2)
    tamanho = arq.tell()
    
    inicio = 0
    fim = (tamanho/registroCEP.size) - 1
    i = 0
    encontrou = False

    print(f"======== Buscando CEP: {sys.argv[1]} ========")
   
    while (inicio <= fim) :
        i += 1
        meio =  int ((inicio + fim) / 2)
        arq.seek(meio * 300)

        line = arq.read(registroCEP.size)
        record = registroCEP.unpack(line)

        if sys.argv[1] == record[5].decode('latin1'):
            encontrou = True
            imprimeLinha(record)
            break
        elif sys.argv[1] < record[5].decode('latin1'):
            fim = meio - 1
        elif sys.argv[1] > record[5].decode('latin1'):
            inicio = meio + 1
    
    if not encontrou:
        print("Cep não encontrado!!!")
    else:
        print(f"Numeros de passos {i}")

    print('========================================')