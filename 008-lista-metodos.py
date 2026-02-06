##### LISTA #####

esporte = ["Futebol", "Basquete", "Golf", "Snowboard","E-game", "Tenis", "Surf", "Voleibol",]

valores = ["🤡", "1" , "10", "Maça"]

num_impar = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41]

#.append -> adicionar valor no final da lista
esporte.append("Futebol")
esporte.append("Badminton")

#.insert(i,x) -> adicionar um valor(x) na posição informada(i)
esporte.insert(1,"Futsal")

#.count -> retorna a quantidade de vezes que um valor se repete
print(esporte.count("Futsal"))

#.remove(x) -> Remove um o valor da lista com base no "Valor"
esporte.remove("Futebol")

#para remover todas as incidencias da palavra "Futebol na lista esporte"
# if "Futebol" in esporte:
#     esporte.remove("Futebol")

#.reversed() -> inverter os valores da lista (o primeiro passa a ser o ultimo e o ultimo passa a ser o primeiro)
esporte.reverse()

esporte.extend(valores)
# esporte.extend(num_impar)
#.sort()
esporte.sort()


# print(f"{valores}")

# para mostrar apenas os valores da lista sem o [] e sem "", e o 'sep=", "' para separa pelo que for informado
print(*esporte, sep=", ")
# print(esporte)

# esporte.clear()
# print(esporte)

print
