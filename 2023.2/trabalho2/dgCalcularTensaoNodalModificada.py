import numpy as np
import sympy as sp
import cmath
def calcularTensaoNodalModificadaSimulacaoDC(listaComponentes, quantidadeNos, quantidadeFonteTensao, simulacao, frequencia, fase=0):
    numElementos = len(listaComponentes)
    matrizCondutancia = np.zeros((quantidadeNos+quantidadeFonteTensao+1, quantidadeNos+quantidadeFonteTensao+1), dtype=complex)
    matrizCondutancia1 = np.zeros((quantidadeNos+quantidadeFonteTensao+1, quantidadeNos+quantidadeFonteTensao+1), dtype=complex)
    vetorEntrada = np.zeros(quantidadeNos+quantidadeFonteTensao+1, dtype=complex)
    for indice, elemento in enumerate(listaComponentes):
        no1 = int(elemento[2]) 
        no2 = int(elemento[3])
        tipo = elemento[0]
        ix=0
        if tipo == 'R':
            valor = elemento[4]
            g = 1 / valor
            matrizCondutancia[no1, no1] += g
            matrizCondutancia[no2, no2] += g
            matrizCondutancia[no1, no2] -= g
            matrizCondutancia[no2, no1] -= g
            #print(matrizCondutancia)
        if tipo == 'C':
            valor = elemento[4]
            g = (2*np.pi*frequencia*valor*1j)
            matrizCondutancia[no1, no1] += g
            matrizCondutancia[no2, no2] += g
            matrizCondutancia[no1, no2] -= g
            matrizCondutancia[no2, no1] -= g
            #print(matrizCondutancia)
        if tipo == 'L':
            valor = elemento[4]
            ix=elemento[5]+quantidadeNos+1
            matrizCondutancia[no1, ix] += 1
            matrizCondutancia[no2, ix] -= 1
            matrizCondutancia[ix, no1] -= 1
            matrizCondutancia[ix, no2] += 1
            matrizCondutancia[ix, ix] += 1j*2*np.pi*frequencia*valor
        elif tipo == 'H':
            valor = elemento[7]
            controlePositivo= elemento[5]
            controleNegativo = elemento[6]
            ix=quantidadeNos+elemento[4]+2
            iy=quantidadeNos+elemento[4]+1
            g = valor
            matrizCondutancia[no1, iy] += 1
            matrizCondutancia[no2, iy] -= 1
            matrizCondutancia[controlePositivo, ix] += 1
            matrizCondutancia[controleNegativo, ix] -= 1
            matrizCondutancia[ix, controlePositivo] -=1
            matrizCondutancia[ix, controleNegativo] +=1
            matrizCondutancia[iy, no1]-=1
            matrizCondutancia[iy, no2]+=1
            matrizCondutancia[iy, ix]+=valor
            
        elif tipo == 'E':
            valor = elemento[7]
            controlePositivo= elemento[5]
            controleNegativo = elemento[6]
            ix=quantidadeNos+elemento[4]+1
            g = valor
            matrizCondutancia[no1, ix] += 1
            matrizCondutancia[no2, ix] -= 1
            matrizCondutancia[ix, no1] -= 1
            matrizCondutancia[ix, no2] += 1
            matrizCondutancia[ix, controlePositivo] +=valor
            matrizCondutancia[ix, controleNegativo] -=valor

        elif tipo == 'F':
            valor = elemento[7]
            controlePositivo= elemento[5]
            controleNegativo = elemento[6]
            g = valor
            ix=quantidadeNos+elemento[4]+1
            matrizCondutancia[no1, ix] += valor
            matrizCondutancia[no2, ix] -= valor
            matrizCondutancia[controlePositivo, ix] += 1
            matrizCondutancia[controleNegativo, ix] -= 1
            matrizCondutancia[ix, controlePositivo] -=1
            matrizCondutancia[ix, controleNegativo] +=1
        elif tipo == 'V':
            if elemento[5]==simulacao:
                if elemento[5]=='AC':
                    fase=(np.pi*elemento[7])/360  
                else:
                    fase=0
                ix=quantidadeNos+elemento[4]+1
                valor = elemento[6] if elemento[5] == 'DC' else 0  # Valor da fonte de tensão
                matrizCondutancia[no1, ix] += 1
                matrizCondutancia[no2, ix] -= 1
                matrizCondutancia[ix, no1] -= 1
                matrizCondutancia[ix, no2] += 1
                vetorEntrada[ix] -= cmath.rect(valor, fase)
        elif tipo == 'I':
            if elemento[4] == simulacao:
                fase=(elemento[6]*2*np.pi)/360
                valor = elemento[5]  # Valor da fonte de tensão
                vetorEntrada[no1] -= cmath.rect(valor, fase)
                vetorEntrada[no2] += cmath.rect(valor, fase)
                #print(matrizCondutancia)
        elif tipo == 'K':
            indutanciaMutua=elemento[8]
            indutanciaPrimaria=elemento[6]
            indutanciaSecundaria=elemento[7]
            no3, no4 = elemento[4], elemento[5]
            n=np.sqrt(elemento[6]/elemento[7])
            k=indutanciaMutua/np.sqrt(indutanciaPrimaria*indutanciaSecundaria)
            if k==1:
                ix=quantidadeNos+elemento[10]
                matrizCondutancia[no1, ix] -= n
                matrizCondutancia[no2, ix] += n
                matrizCondutancia[no3, ix] += 1
                matrizCondutancia[no4, ix] -= 1
                matrizCondutancia[ix, no1] += n
                matrizCondutancia[ix, no2] -= n
                matrizCondutancia[ix, no3] -= 1
                matrizCondutancia[ix, no4] += 1
            elif k<1:
                iy=quantidadeNos+elemento[10]
                ix=quantidadeNos+elemento[10]-1
                matrizCondutancia[no1][ix]+=1
                matrizCondutancia[no2][ix]-=1
                matrizCondutancia[no3][iy]+=1
                matrizCondutancia[no4][iy]-=1
                matrizCondutancia[ix][no1]-=1
                matrizCondutancia[ix][no2]+=1
                matrizCondutancia[ix][ix]+=1j*2*np.pi*frequencia*indutanciaPrimaria
                matrizCondutancia[ix][iy]+=1j*2*np.pi*frequencia*indutanciaMutua
                matrizCondutancia[iy][no3]-=1
                matrizCondutancia[iy][no4]+=1
                matrizCondutancia[iy][ix]+=1j*2*np.pi*frequencia*indutanciaMutua
                matrizCondutancia[iy][iy]+=1j*2*np.pi*frequencia*indutanciaSecundaria
        # Adicione condições para outros tipos de componentes (capacitores, indutores, fontes dependentes) se necessário
    # Resolva o sistema de equações lineares
    #print(matrizCondutancia)
    matrizCondutancia = np.delete(matrizCondutancia, 0, axis=0)
    matrizCondutancia = np.delete(matrizCondutancia, 0, axis=1)
    vetorEntrada = np.delete(vetorEntrada, 0)
    tensaoNodal = np.linalg.solve(matrizCondutancia, vetorEntrada)
    return tensaoNodal

