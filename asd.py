lista = []
while True:
    antonio = input("informe a modalidade")
    if antonio == "fim":
        break
    lista.append(antonio)
lista.sort()
print(lista)
