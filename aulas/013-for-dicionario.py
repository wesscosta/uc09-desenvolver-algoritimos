# Dicionario aluno -> Chave / Valor

aluno = {
    "nome": "Antonio",
    "sobrenome": "Silva",
    "idade": 30,
    "altura": 1.70,
    "peso": 70
}


# Atualizar o valor da chave "idade" para 50
aluno["idade"] = 50

# Imprimi as chaves do dicionário
for i in aluno:
    print(i)

# Imprimi os valores do dicionário
for i in aluno.values():
    print(i)
    
# Imprimi as chaves e os valores do dicionário
for i in alunos.get("aluno").values():
    print(i)
