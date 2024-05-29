import numpy as np
def lerNetlist(nomeArquivo):
    netlistCircuito = []
    with open(f'./netlists/{nomeArquivo}', 'r') as arquivo:
        for linha in arquivo:
            if linha.startswith('*') or not linha.strip():
                continue  # Ignora linhas de comentário e linhas vazias
            componentes = linha.split()
            tipoComponente = componentes[0][0]
            idComponente = int(componentes[0][1:])
            no1, no2 = int(componentes[1]), int(componentes[2])
            if tipoComponente=='R':
                valor = float(componentes[3])
                netlistCircuito.append([tipoComponente, idComponente, no1, no2, valor])
            elif tipoComponente=='I':
                valor = float(componentes[4])
                netlistCircuito.append([tipoComponente,idComponente, no1, no2, 'DC', valor])
            elif tipoComponente=='G':
                controle_pos, controle_neg = int(componentes[4]), int(componentes[5])
                valor = int(componentes[5])
                controle_pos=int(componentes[3])
                controle_neg=int(componentes[4])
                netlistCircuito.append([tipoComponente, idComponente, no1, no2, controle_pos, controle_neg, valor])
    return netlistCircuito



