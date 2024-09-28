import random
palpites = []
mamiferos = {1 : 'elefante', 2 : 'leão', 3 : 'baleia', 4 : 'macaco', 5 : 'cavalo', 6 : 'urso'}
aves = {1 : 'periquito', 2 : 'arara', 3 : 'avestruz', 4 : 'galinha', 5 : 'águia', 6 : 'pelicano'}
répteis = {1 : 'lagarto', 2 : 'jacaré', 3 : 'crocodilo', 4 : 'camaleão', 5 : 'iguana', 6 : 'cobra'}
peixes = {1 : 'tilapia', 2 : 'pacu', 3 : 'peixe_boi', 4 : 'peixe_bolha', 5 : 'peixe_palhaço', 6 : 'baiacu'}
anfibios = {1 : 'sapo', 2 : 'perereca', 3 : 'rã', 4 : 'salamandras', 5 : 'tritão', 6 : 'cecílias'}
while True:
    num1 = int(input("Escolha a categoria de Animais: 1 - mamifero, 2 - aves, 3 - repteis, 4 - peixes, 5 - anfibios:  "))
    if num1 > 5:
        print("Erro")
    elif num1 < 1:
        print("Erro")
    else:
        break
if num1 == 1:
    numrandom = random.choice(mamiferos)
if num1 == 2:
    numrandom = random.choice(aves)
if num1 == 3:
    numrandom = random.choice(répteis)
if num1 == 4:
    numrandom = random.choice(peixes)
if num1 == 5:
    numrandom = random.choice(anfibios)
print("------- Vamos Iniciar o Jogo! --------------\n")
dica = len(numrandom)
while True:
    print(f"Dica: A palavra tem {dica} letras")
    palpitei = input("Tente adivinhar a palavra: ").lower()
    palpites.append(palpitei)
    if palpitei == numrandom:
        break
    else:
        print("Palpite errado.")
        print("Tente novamente.\n")
        continue
print("Parabéns! Você acertou a palavra.")
tentativas = len(palpites)
print(f"Número de palpites: {tentativas}")
print(f"Palpites realizados: {palpites}")
