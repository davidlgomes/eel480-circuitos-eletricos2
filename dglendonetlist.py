import numpy as np
def lendoNetlist(nomeArquivo):
    netlistCircuito = []
    with open(nomeArquivo, 'r') as arquivo:
        for linha in arquivo:
            if linha.startswith('*') or not linha.strip():
                continue  # Ignora linhas de comentário e linhas vazias
            componentes = linha.split()
            if len(componentes) >= 3:
                tipoComponente = componentes[0][0]
                no1, no2 = int(componentes[1]), int(componentes[2])
                if tipoComponente in ('R', 'I', 'G') and len(componentes) >= 4:
                    valores = [no1, no2] + [float(valor) if valor != 'DC' else valor for valor in componentes[3:]]
                    netlistCircuito.append([tipoComponente] + valores)
    return netlistCircuito
