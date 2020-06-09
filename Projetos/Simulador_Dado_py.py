import random


"""

Simulador de Dado:


"""


n1 = "sim"


jogar = input('Voce gostaria de jogar o dado?: ')

while jogar.lower() == n1:
    print(int(random.randrange(1,6)))
    jogar = input('Voce gostaria de jogar o dado?: ')

print('Obrigado por ter jogado')






