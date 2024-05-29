import numpy as np
import math
import cmath
import matplotlib.pyplot as plt
from dgLendoNetlist import lerNetlist
from dgCalcularTensaoNodalModificada import calcularTensaoNodalModificadaSimulacaoDC
#from dgCalcularTensaoNodalModificada import calcularFrequenciaModuloFaseAnaliseNodalModificadaSimulacaoAC

def main(arqNetlist, tipo, nos, parametros):
    listaComponentes = lerNetlist(arqNetlist)
    quantidadeNos=0
    quantidadeFonteTensao=0
    if tipo == 'DC':
        for componente in listaComponentes:
            if componente[0]=='V':
                quantidadeFonteTensao+=1
            elif componente[0]=='E' or componente[0]=='F' or componente[0]=='L':
                quantidadeFonteTensao+=1
            elif componente[0]=='H':
                quantidadeFonteTensao+=2
            elif componente[0]=='K':
                indutanciaMutua=componente[8]
                indutanciaPrimaria=componente[6]
                indutanciaSecundaria=componente[7]
                n=np.sqrt(componente[6]/componente[7])
                k=indutanciaMutua/np.sqrt(indutanciaPrimaria*indutanciaSecundaria)
                if k==1:
                    quantidadeFonteTensao+=1
                elif k<1:
                    quantidadeFonteTensao+=2
        quantidadeNos = max(int(componente[2]), int(componente[3]))
        tensoesNodais = calcularTensaoNodalModificadaSimulacaoDC(listaComponentes, quantidadeNos, quantidadeFonteTensao, simulacao='DC', frequencia=0, fase=0)
        tensaoNodal=[tensoesNodais[no-1] for no in nos]
        return tensaoNodal
    elif tipo=='AC':
        tensoesNodais=[[]for _ in range(len(nos))]
        tensaoNodal=[[]for _ in range(len(nos))]
        fases=[[] for _ in range(len(nos))]
        frequenciaArray=[]
        modulo=[]
        amplitudes=[[] for _ in range(len(nos))]
        teste=[]
        quantidadePontos=(10.0*parametros[1])/(parametros[0]*parametros[2])
        frequencias=np.logspace(np.log10(parametros[0]), np.log10(parametros[1]), int(quantidadePontos))
        for indice, frequencia in enumerate(frequencias):
            quantidadeFonteTensao=0
            for componente in listaComponentes:
                if componente[0]=='V':
                    quantidadeFonteTensao+=1
                elif componente[0]=='E' or componente[0]=='F' or componente[0]=='L':
                    quantidadeFonteTensao+=1
                elif componente[0]=='H':
                    quantidadeFonteTensao+=2
                elif componente[0]=='K':
                    indutanciaMutua=componente[8]
                    indutanciaPrimaria=componente[6]
                    indutanciaSecundaria=componente[7]
                    n=np.sqrt(componente[6]/componente[7])
                    k=indutanciaMutua/np.sqrt(indutanciaPrimaria*indutanciaSecundaria)
                    if k==1:
                        quantidadeFonteTensao+=1
                    elif k<1:
                        quantidadeFonteTensao+=2
            quantidadeNos = max(int(componente[2]), int(componente[3]))
            tensoesNodais.append([calcularTensaoNodalModificadaSimulacaoDC(listaComponentes, quantidadeNos, quantidadeFonteTensao, simulacao='AC', frequencia=frequencia, fase=0)[no-1] for no in nos])
        plt.plot(tensoesNodais[1])
        plt.show()
        return tensoesNodais


