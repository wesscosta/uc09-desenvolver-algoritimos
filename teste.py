letras = ["a","b","a","c","b","a","d","c"]
letras_usadas = []

for letra_atual in letras:
    if letra_atual not in letras_usadas:
        total = 0
        
        for letras_lista in letras:
            if letras_lista == letra_atual:
               total = total + 1
            
        print(letra_atual, "aparece", total ,"vezes") 
        letras_usadas.append(letra_atual)        
