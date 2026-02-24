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
    },
   "aluno03":{
        "nome": "João",
        "sobrenome": "Pereira",
        "idade": 28,
        "altura": 1.80,
        "peso": 80
        },
    "aluno04":{
        "nome": "Ana",
        "sobrenome": "Gomes",
        "idade": 22,
        "altura": 1.60,
        "peso": 55
    },
    "aluno05":{
        "nome": "Carlos",
        "sobrenome": "Lima",
        "idade": 35,
        "altura": 1.75,
        "peso": 90
      }
}
alunos["aluno02"]["idade"]


# lista_alunos = ["jose", "maria", "joao", "ana", "carlos"]

# for i in lista_alunos:
#     print(i)


aluno01 = {
    "nome": "Antonio",
    "sobrenome": "Silva",
    "idade": 30,
    "altura": 1.70,
    "peso": 70
}
aluno01["idade"] = 50

# for i in aluno01:
#     print(i)

# for i in aluno01.values():
#     print(i)
    
for i in alunos.get("aluno01").values():
    print(i)
