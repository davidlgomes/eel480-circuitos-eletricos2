import numpy as np
def calcularTensaoNodalSimples(listaComponentes, quantidadeNos):
    matrizCondutancia = np.zeros((quantidadeNos+1, quantidadeNos+1))  # Matriz de condutância
    matrizCorrente = np.zeros((quantidadeNos+1, 1))           # Vetor de correntes
    for componente in listaComponentes:
        no1 = componente[2]-1
        no2 = componente[3]-1

        if componente[0] == 'R':
            matrizCondutancia[no1][no1] += 1/componente[4]
            matrizCondutancia[no2][no2] += 1/componente[4]
            matrizCondutancia[no1][no2] -= 1/componente[4]
            matrizCondutancia[no2][no1] -= 1/componente[4]

        elif componente[0] == 'I':
            matrizCorrente[no1] -= componente[5]
            matrizCorrente[no2] += componente[5]

        elif componente[0] == 'G':
            controlePositivo = int(componente[4]) 
            controleNegativo = int(componente[5]) 
            matrizCondutancia[no1][controlePositivo] += componente[6]
            matrizCondutancia[no2][controlePositivo] -= componente[6]
            matrizCondutancia[no1][controleNegativo] -= componente[6]
            matrizCondutancia[no2][controleNegativo] += componente[6]
    # Remove a linha e coluna do nó de terra
    matrizCondutancia = np.delete(matrizCondutancia, -1, axis=0)
    matrizCondutancia = np.delete(matrizCondutancia, -1, axis=1)
    matrizCorrente = np.delete(matrizCorrente, -1)

    # Resolve o sistema de equações lineares para encontrar as tensões nodais
    tensaoNodal = np.linalg.solve(matrizCondutancia, matrizCorrente)
    return tensaoNodal