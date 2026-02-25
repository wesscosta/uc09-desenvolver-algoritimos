dicionario = {}
lista = []

for i in range(5):
    pessoa = {
    "nome": input("Digite o nome: "),
    "sobrenome":input("Digite o sobrenome: "),
    "idade":int(input("Digite a idade: ")),
   }
    
    dicionario[f"pessoa{i+1}"] = pessoa
    lista.append(pessoa)
    
    
print(dicionario)
print(lista)
