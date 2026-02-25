# #Dicionario -> Chave / Valor
# minha_lista = {
#         "nome": "Antonio",
#         "sobrenome": "Silva",
#         "idade": 30
#     }

# #nome, sobrenome, idade, altura, peso

#################################
# Dicionário dentro de Dicionário
#################################

alunos = {
    "aluno01":{
        "nome": "Antonio",
        "sobrenome": "Silva",
        "idade": 30,
        "altura": 1.70,
        "peso": 70
    },
   "aluno02":{
        "nome": "Maria",
        "sobrenome": "Santos",
        "idade": 25,
        "altura": 1.65,
        "peso": 60
    }
}
print(alunos["aluno02"]["sobrenome"])


#################################
# Dicionário dentro de Lista
#################################

# alunos = [
#     {
#         "nome": "Antonio",
#         "sobrenome": "Silva",
#         "idade": 30,
#         "altura": 1.70,
#         "peso": 70
#     },
#    {
#         "nome": "Maria",
#         "sobrenome": "Santos",
#         "idade": 25,
#         "altura": 1.65,
#         "peso": 60
#     }
# ]
# print(alunos[1]["sobrenome"])
