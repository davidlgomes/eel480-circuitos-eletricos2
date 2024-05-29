import numpy as np

def lerNetlist(nomeArquivo):
    netlistCircuito = []
    with open(nomeArquivo, 'r') as arquivo:
        for linha in arquivo:
            if linha.startswith('*') or not linha.strip():
                continue  # Ignora linhas de comentário e linhas vazias

            componentes = linha.split()
            tipoComponente = componentes[0][0]
            idComponente = componentes[0][1:]
            no1, no2 = int(componentes[1]), int(componentes[2])

            if tipoComponente in ('R', 'C', 'L'):
                valor = float(componentes[3])
                netlistCircuito.append([tipoComponente, no1, no2, valor])
            elif tipoComponente=='V':
                if componentes[3] == 'AC':
                    amplitude = float(componentes[4])
                    fase = float(componentes[5])
                    netlistCircuito.append([tipoComponente, no1, no2, 'AC', amplitude, fase])
                elif componentes[3] == 'DC':
                    valor = float(componentes[4])
                    netlistCircuito.append([tipoComponente, no1, no2, 'DC', valor])
            elif tipoComponente=='I':
                if componentes[3] == 'AC':
                    amplitude = float(componentes[4])
                    fase = float(componentes[5])
                    netlistCircuito.append([tipoComponente, no1, no2, 'AC', amplitude, fase])
                elif componentes[3] == 'DC':
                    valor = float(componentes[4])
                    netlistCircuito.append([tipoComponente, no1, no2, 'DC', valor])

            elif tipoComponente in ('F', 'H', 'K'):
                controle_pos, controle_neg = int(componentes[3]), int(componentes[4])
                valor = float(componentes[5])
                netlistCircuito.append([tipoComponente, no1, no2, controle_pos, controle_neg, valor])

    return netlistCircuito

def calcularEstampas(listaComponentes, quantidadeNos):
    # Inicializa as matrizes de condutância e corrente
    matrizCondutancia = np.zeros((quantidadeNos, quantidadeNos))
    matrizCorrente = np.zeros((quantidadeNos, 1))

    for componente in listaComponentes:
        tipoComponente = componente[0]
        no1, no2 = int(componente[1]) - 1, int(componente[2]) - 1
        if tipoComponente == 'R':
            valor = componente[3]
            # Estampa para resistores
            g = 1 / valor
            matrizCondutancia[no1, no1] += g
            matrizCondutancia[no2, no2] += g
            matrizCondutancia[no1, no2] -= g
            matrizCondutancia[no2, no1] -= g

        elif tipoComponente == 'V':
            valor = componente[4]
            # Estampa para fontes de tensão
            matrizCondutancia[no1, no1] += 1
            matrizCondutancia[no2, no2] += 1
            matrizCondutancia[no1, no2] -= 1
            matrizCondutancia[no2, no1] -= 1
            matrizCorrente[no1] -= valor
            matrizCorrente[no2] += valor

    return matrizCondutancia, matrizCorrente

def resolverSistema(matrizCondutancia, matrizCorrente):
    try:
        # Solucionar o sistema de equações usando numpy.linalg.solve
        matrizTensao = np.linalg.solve(matrizCondutancia, matrizCorrente)
        return matrizTensao.flatten()
    except np.linalg.LinAlgError:
        print("Matriz de condutância é singular. Verifique seu circuito para curtos-circuitos ou configurações inadequadas.")
        return None

def main(arqNetlist, quantidadeNos):
    listaComponentes = lerNetlist(arqNetlist)
    matrizCondutancia, matrizCorrente = calcularEstampas(listaComponentes, quantidadeNos)
    tensaoNodal = resolverSistema(matrizCondutancia, matrizCorrente)
    return tensaoNodal

# Exemplo de uso
quantidadeNos = 3  # Defina o número de nós do seu circuito
arquivoNetlist = 'netlistDC1.txt'  # Nome do arquivo com o netlist do circuito
resultado = main(arquivoNetlist, quantidadeNos)
print("Tensões nodais:", resultado)
