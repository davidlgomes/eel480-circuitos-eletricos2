import numpy as np
def calcularTensaoNodal(listaComponentes, quantidadeNos):
    matrizCondutancia = np.zeros((quantidadeNos, quantidadeNos))  # Matriz de condutância
    matrizCorrente = np.zeros((quantidadeNos, 1))           # Vetor de correntes

    for componente in listaComponentes:
        no1 = componente[1] - 1
        no2 = componente[2] - 1

        if componente[0] == 'R':
            matrizCondutancia[no1][no1] += 1 / componente[3]
            matrizCondutancia[no2][no2] += 1 / componente[3]
            matrizCondutancia[no1][no2] -= 1 / componente[3]
            matrizCondutancia[no2][no1] -= 1 / componente[3]

        elif componente[0] == 'I':
            matrizCorrente[no1] -= componente[4]
            matrizCorrente[no2] += componente[4]

        elif componente[0] == 'G':
            controlePositivo = int(componente[3]) - 1
            controleNegativo = int(componente[4]) - 1
            matrizCondutancia[no1][controlePositivo] += componente[5]
            matrizCondutancia[no2][controlePositivo] -= componente[5]
            matrizCondutancia[no1][controleNegativo] -= componente[5]
            matrizCondutancia[no2][controleNegativo] += componente[5]

    # Remove a linha e coluna do nó de terra
    matrizCondutancia = np.delete(matrizCondutancia, -1, axis=0)
    matrizCondutancia = np.delete(matrizCondutancia, -1, axis=1)
    matrizCorrente = np.delete(matrizCorrente, -1)

    # Resolve o sistema de equações lineares para encontrar as tensões nodais
    tensaoNodal = np.linalg.solve(matrizCondutancia, matrizCorrente)
    return tensaoNodal