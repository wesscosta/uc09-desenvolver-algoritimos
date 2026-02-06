## condicionais (if-elif-else) + FOR com brack e continue

for x in range(50):
    if x == 2: continue
    if x == 4: break
    
    print(f"{'#'*10}, ESSA É A {x} VEZ {'#'*10}")
  
    dia = input("Digite um dia: ")
    
    
    if dia.lower() == "segunda":
        print(f"Começou a Sofrencia!!!")
        
    elif dia.lower() == "terça":
        print(f"Ta mais longe do que perto!!")
        
    elif dia.lower() == "quarta":
        print(f"Hoje tem jogo da SELEÇÃO!!!")

    elif dia.upper() == "QUINTA":
        print(f"Semana tá acabandooo!!!")
        
    elif dia.upper() == "SEXTA":
        print(f"SEXTOUUUUUUUUUUUUUUUUUUUUUU!!!")
    elif dia == "":
        print(f"EU VI, TU NÃO DIGITOU NADA!!!!!")
        
    else:
        print(f"Fimmmmmmmmmmmmm de semanaaaaaaaaaaaaaaaaaaaa!!!")
