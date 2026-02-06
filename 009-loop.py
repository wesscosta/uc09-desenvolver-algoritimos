#Laços de Repetição | Estrutura de Repetição | Loop
# for

itens = ["50", "cha", "Arroz", "Caixa", "Zebra","Café"]    

for x in itens:
    print(x)
"""
 "50"
 "cha"
 "Arroz"
 "Caixa"
 "Zebra"
 "Café"
"""

for x in itens[3]:
    print(x)

"""
 C
 a
 i
 x
 a
"""

"""
#Forma Errada

for x in 50:
    print(itens[x])

######################

#Forma Correta: usando a função ranger
#Função ranger -> 3 variações: (start, stop, step)
#1ªforma:  range(10) -> [0,1,2,3,4,5,6,7,8,9] 
#2ªforma:  range(2,10) -> [2,3,4,5,6,7,8,9] 
#3ªforma:  range(2,10,2) -> [2,4,6,8] 

"""


#Ex: Imprimir do 1 ao 100, saltando de 10 em 10 e no final imprima essa lista ao contrario
nova_lista=[]
for i in range(1,101,10):
    nova_lista.append(i)
    
nova_lista.reverse()
print(*nova_lista)

