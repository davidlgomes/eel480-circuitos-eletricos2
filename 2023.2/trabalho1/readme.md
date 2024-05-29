# EEL480 - Análise Nodal Simples

Este programa foi desenvolvido para calcular as tensões nodais em circuitos elétricos usando o método de estampa em análise nodal simples.

## Estrutura do Projeto

O projeto está organizado nos seguintes arquivos:

1. **dgchamada.py**: Este arquivo contém as chamadas da função `main` com os nomes dos arquivos específicos.
2. **trab1davidgomes.py**: Este arquivo contém o código principal da aplicação.
3. **dglendonetlist.py**: Este arquivo contém o código para ler as netlists localizadas na pasta local, a fim de processar as informações.
4. **dgcalculartensaonodal.py**: Neste arquivo, os dados lidos em `dglendonetlist.py` são usados para calcular as tensões nodais usando a análise nodal simples.
5. **netlist0.txt**: Contém a netlist gerada pelo circuito 0.
6. **netlist1.txt**: Contém a netlist gerada pelo circuito 1.
7. **netlist2.txt**: Contém a netlist gerada pelo circuito 2.
8. **netlist3.txt**: Contém a netlist gerada pelo circuito 3.

## Componentes Aceitos

O programa aceita três tipos de componentes:

1. Fonte de corrente controlada por tensão
   - Formato: `IX <"Nó A"> <"Nó B"> <"ACouDC"> <"Valor">`, onde X é a numeração do componente.
2. Fonte de corrente independente
   - Formato: `GX <"Nó A"> <"Nó B"> <"NóDeControlePositivo"> <"NóDeControleNegativo"> <"Valor">`, onde X é a numeração do componente.
3. Resistor
   - Formato: `RX <"Nó A"> <"Nó B"> <"Valor">`, onde X é a numeração do componente.

## Executando o Programa

Para executar o programa, use o arquivo `dgchamada.py`.

Exemplo:
```shell
python dgchamada.py
