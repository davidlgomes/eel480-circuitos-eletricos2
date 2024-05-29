import numpy as np
def lerNetlist(nomeArquivo):
    netlistCircuito = []
    ix=0
    with open(nomeArquivo, 'r') as arquivo:
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
            if tipoComponente=='C':
                valor = float(componentes[3])
                netlistCircuito.append([tipoComponente,idComponente, no1, no2, valor])
                break
            if tipoComponente=='L':
                float(componentes[3])
                netlistCircuito.append([tipoComponente,idComponente, no1, no2, valor, ix])
                ix+=1
                break
            elif tipoComponente=='V':
                if componentes[3] == 'AC':
                    amplitude = float(componentes[4])
                    fase = float(componentes[5])
                    netlistCircuito.append([tipoComponente, idComponente, no1, no2, ix, 'AC', amplitude, fase])
                    ix+=1
                elif componentes[3] == 'DC':
                    valor = float(componentes[4])
                    netlistCircuito.append([tipoComponente,idComponente, no1, no2, ix, 'DC', valor])
                    ix+=1
            elif tipoComponente=='I':
                if componentes[3] == 'AC':
                    amplitude = float(componentes[4])
                    fase = float(componentes[5])
                    netlistCircuito.append([tipoComponente, idComponente, no1, no2, 'AC', amplitude, fase])
                elif componentes[3] == 'DC':
                    valor = float(componentes[4])
                    netlistCircuito.append([tipoComponente,idComponente, no1, no2, 'DC', valor])
            elif tipoComponente=='E':
                controle_pos, controle_neg = int(componentes[4]), int(componentes[5])
                valor = int(componentes[5])
                controle_pos=int(componentes[3])
                controle_neg=int(componentes[4])
                netlistCircuito.append([tipoComponente, idComponente, no1, no2, ix, controle_pos, controle_neg, valor])
                ix+=1
            elif tipoComponente=='G' or tipoComponente=='F':
                controle_pos, controle_neg = int(componentes[4]), int(componentes[5])
                valor = int(componentes[5])
                controle_pos=int(componentes[3])
                controle_neg=int(componentes[4])
                netlistCircuito.append([tipoComponente, idComponente, no1, no2, ix, controle_pos, controle_neg, valor])
                ix+=1
            elif tipoComponente=='H':
                controle_pos, controle_neg = int(componentes[4]), int(componentes[5])
                valor = int(componentes[5])
                controle_pos=int(componentes[3])
                controle_neg=int(componentes[4])
                netlistCircuito.append([tipoComponente, idComponente, no1, no2, ix, controle_pos, controle_neg, valor])
                ix+=2
            elif tipoComponente=='K':
                no1IndutorPrimario, no2IndutorPrimario, indutanciaL1=int(componentes[1]), int(componentes[2]), float(componentes[5])
                no1IndutorSecundario, no2IndutorSecundario, indutanciaL2=int(componentes[3]), int(componentes[4]), float(componentes[6])
                indutanciaMutua=float(componentes[7])
                k=indutanciaMutua/np.sqrt(indutanciaL1*indutanciaL2)
                if k==1:
                    ix+=1
                elif k<1:
                    ix+=2
                netlistCircuito.append([tipoComponente, idComponente, no1IndutorPrimario, no2IndutorPrimario, no1IndutorSecundario, no2IndutorSecundario, indutanciaL1,indutanciaL2,indutanciaMutua, k, ix])
    return netlistCircuito



