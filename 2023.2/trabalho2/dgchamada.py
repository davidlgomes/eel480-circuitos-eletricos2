from trab2davidgomes import main
# print("Análise DC:")
# print(main('netlistDC1.txt', 'DC', [2], [])) #Resultado esperado: [6.]
# print(main('netlistDC2.txt', 'DC', [2,3,5,7,9,10], [])) #Resultado esperado: [ 8, 1, 8.4, 0.93333333, -5.6, -3.73333333
# print(main('netlistDC3.txt', 'DC', [1,2,3,4,5,6,7], [])) #Resultado esperado: [10. , 5.7554841,  2.49323451,  4.37608413,  2.28100871, 5.7554841, 6.37608413]
# print(main('netlistDC4.txt', 'DC', [2], [])) #Resultado esperado: [6.]
# print(main('netlistDC5.txt', 'DC', [2], [])) #Resultado esperado: [10.]
# print(main('netlistDC6.txt', 'DC', [3,4,5], [])) #Resultado esperado: [0.5, 0, 0]


print('\n\n\n')
print("Análise AC:")
print("1:")
print(main('./netlistAC1.txt','AC',[1], [0.01, 100, 100]))
#print("2:")
#print(main('./netlistAC2.txt','AC',[1], [0.01, 200, 100]))
#print("3:")
#print(main('./netlistAC3.txt','AC',[2], [0.01, 100, 100]))
#print("4:")
#print(main('./netlistAC4.txt','AC',[2,3], [0.01, 500, 1000]))
#print("5:")
#print(main('./netlistAC5.txt','AC',[3], [0.01, 1000, 1000]))
#print("6:")
#print(main('./netlistAC6.txt','AC',[2,5], [0.01, 2e3, 1000]))
#print("7:")
#print(main('./netlistAC7.txt','AC',[2,7], [0.01, 100, 1000]))
#print("8:")
#print(main('./netlistAC8.txt','AC',[4], [100, 100e3, 100]))
#print("9:")
#print(main('./netlistAC9.txt','AC',[2,3,4,5,6], [0.01, 100, 1000]))
#print("10:")
#print(main('./netlistAC10.txt','AC',[4,5], [0.01, 500, 1000]))
