from dglendonetlist import lendoNetlist
from dgcalculartensaonodal import calcularTensaoNodal
def main(arqNetlist):
    listaComponentes = lendoNetlist(arqNetlist)
    quantidadeNos = max(max(componente[1], componente[2]) for componente in listaComponentes)
    tensaoNodal = calcularTensaoNodal(listaComponentes, quantidadeNos + 1)  # Adiciona o nó de terra
    for i, tensaoNodal in enumerate(tensaoNodal):
        print(f'e{i + 1} = {tensaoNodal:.15f} V')
    return ''