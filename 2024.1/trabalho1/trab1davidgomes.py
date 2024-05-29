import numpy as np
import math
import cmath
from dgLendoNetlist import lerNetlist
from dgCalcularTensaoNodal import calcularTensaoNodalSimples
def main(arqNetlist):
    listaComponentes = lerNetlist(arqNetlist)
    quantidadeNos =max(max(componente[2], componente[3]) for componente in listaComponentes)
    tensoesNodais = calcularTensaoNodalSimples(listaComponentes, quantidadeNos)
    return tensoesNodais