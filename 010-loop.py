#Laços de Repetição | Estrutura de Repetição | Loop
# for & while

itens = ["50", "cha", "Arroz", "Caixa", "Zebra","Café"]    

# for x in itens:
#     print(x)
"""
"50"
"cha"
"Arroz"
"Caixa"
"Zebra"
"Café"
"""

# for x in itens[3]:
#     print(x)

"""Caixa"""



# for x in 50:
#     print(itens[x])


#Função Ranger (3 variações: start, stop, step)
# lista_numeros = range(2,10,5)
# [2,12,22,32,42]


#Imprimir os do 1 ao 100, saltando de 10 em 10 e no final imprima essa lista ao contrario, um valor por vez
nova_lista=[]
for i in range(1,101,10):
    nova_lista.append(i)
    
nova_lista.reverse()

for j in nova_lista:
    print(j)

