import numpy as np
import matplotlib.pyplot as plt
from dgLendoNetlist import lerNetlist
from dgCalcularTensaoNodalModificada import calcularTensaoNodalModificada
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
        tensoesNodais = calcularTensaoNodalModificada(listaComponentes, quantidadeNos, quantidadeFonteTensao, simulacao='DC', frequencia=0, fase=0)
        tensaoNodal=[tensoesNodais[no-1] for no in nos]
        return tensaoNodal
    elif tipo=='AC':
        tensoesNodais = []
        quantidadePontos = (10.0 * parametros[1]) / (parametros[0] * parametros[2])
        frequencias = np.logspace(np.log10(parametros[0]), np.log10(parametros[1]), int(quantidadePontos))
        amplitudes = []
        fases=[]
        for indice, frequencia in enumerate(frequencias):
            quantidadeFonteTensao = 0
            for componente in listaComponentes:
                if componente[0] == 'V':
                    quantidadeFonteTensao += 1
                elif componente[0] in ['E', 'F', 'L']:
                    quantidadeFonteTensao += 1
                elif componente[0] == 'H':
                    quantidadeFonteTensao += 2
                elif componente[0] == 'K':
                    indutanciaMutua = componente[8]
                    indutanciaPrimaria = componente[6]
                    indutanciaSecundaria = componente[7]
                    k = indutanciaMutua / np.sqrt(indutanciaPrimaria * indutanciaSecundaria)
                    if k == 1:
                        quantidadeFonteTensao += 1
                    elif k < 1:
                        quantidadeFonteTensao += 2
            quantidadeNos = max(int(componente[2]), int(componente[3]))
            tensoes = calcularTensaoNodalModificada(listaComponentes, quantidadeNos, quantidadeFonteTensao, simulacao='AC', frequencia=frequencia, fase=0)
            tensoesNodais.append([tensoes[no - 1] for no in nos])

        for tensoes in tensoesNodais:
            amplitudes.append([20 * np.log10(abs(tensao)) for tensao in tensoes])
            fases.append([np.angle(tensao) for tensao in tensoes])
        # Example plot
        plt.figure()
        for indice, no in enumerate(nos):
            plt.plot(frequencias, [amplitude[indice] for amplitude in amplitudes], label=f'Módulo Nó {no}')
            plt.plot(frequencias, [np.degrees(fase[indice]) for fase in fases], label=f'Fase Nó {no}')
        plt.xscale('log')
        plt.xlabel('Frequencia (Hz)')
        plt.ylabel('Amplitude (dB)')
        plt.title('Análise em Frequência')
        plt.legend()
        plt.grid()
        plt.show()

        return amplitudes


