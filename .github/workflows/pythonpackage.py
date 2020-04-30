from random import choice

#Rodar De novo
RD = 1 
while (RD==1):
      #Valor dos Dados
      dado1 = [1,2,3,4,5,6]
      dado2 = [1,2,3,4,5,6]
      #Apresentação
      print("╔═══════════════════════════════════════════════════════════════════════╗")
      print(" Bem-vindo a um dos milhares de Cassino de Las Vegas!")
      print(" Para começar a jogar é preciso que digite uma aposta.")
      print(" Se a soma do valor dos dados de 6 lados for igual a aposta, voce ganha!")
      print("╚═══════════════════════════════════════════════════════════════════════╝")
      #Valor da Aposta
      print()
      aposta = int(input("Vamos la, digite o valor da aposta que seja entre 2 a 12: "))
      print()
      if aposta > 12 or aposta < 2: #Caso o Jogador coloque um valor diferente
            print("──────────────────────────────────────────")
            print("POR FAVOR INSIRA UM NÚMERO ENTRE 2 A 12!!!")
            print("──────────────────────────────────────────")
            print("Vamos de novo...")
            print()
      else:
            print("Ok, agora iremos rodar os 2 dados...")
            resultado1 = choice(dado1)
            resultado2 = choice(dado2)
            print()
            print("O número do primeiro dado é:", resultado1)
            print("O número do segundo dado é:", resultado2)
            #Soma dos dados
            soma = resultado1 + resultado2
            print("portanto, a soma deles é... ", soma)
            print()

            if soma == aposta:
                  print("PARABENS! Você ganhou a aposta!")
            else:
                  print("Que triste você perdeu a aposta :/")

            print()
            
            print("Quer jogar Novamente?")
            RD = int(input("Se sim, tecle 1, se não, tecle qualquer numero: "))

