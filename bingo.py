import random

cartela1 = []
cartela2 = []
cartela3 = []
cartela4 = []
cartela5 = []
sorteados = []
vencedores = []

while not cartela1 or not cartela2 or not cartela3 or not cartela4 or not cartela5:
    cartela1 = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    if cartela1[0] == cartela1[1] or cartela1[0] == cartela1[2] or cartela1[1] == cartela1[2]:
        cartela1 = []
        continue
    cartela2 = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    if cartela2[0] == cartela2[1] or cartela2[0] == cartela2[2] or cartela2[1] == cartela2[2]:
        cartela2 = []
        continue
    cartela3 = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    if cartela3[0] == cartela3[1] or cartela3[0] == cartela3[2] or cartela3[1] == cartela3[2]:
        cartela3 = []
        continue
    cartela4 = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    if cartela4[0] == cartela4[1] or cartela4[0] == cartela4[2] or cartela4[1] == cartela4[2]:
        cartela4 = []
        continue
    cartela5 = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    if cartela5[0] == cartela5[1] or cartela5[0] == cartela5[2] or cartela5[1] == cartela5[2]:
        cartela5 = []
        continue
    
    if cartela1 == cartela2:
        cartela2 = []
        continue
    if cartela2 == cartela3 or cartela1 == cartela3:
        cartela3 = []
        continue
    if cartela3 == cartela4 or cartela4 == cartela2 or cartela4 == cartela1:
        cartela4 = []
        continue
    if cartela5 == cartela4 or cartela5 == cartela3 or cartela5 == cartela2 or cartela5 == cartela1:
        cartela5 = []
        continue

cartela1.sort()
cartela2.sort()
cartela3.sort()
cartela4.sort()
cartela5.sort()

print("Aqui estão as cartelas iniciais:")
print(f"Cartela 1: {cartela1}")
print(f"Cartela 2: {cartela2}")
print(f"Cartela 3: {cartela3}")
print(f"Cartela 4: {cartela4}")
print(f"Cartela 5: {cartela5}")

while cartela1 or cartela2 or cartela3 or cartela4 or cartela5:
    numero_sorteado = 0
    sorteio = input("Digite 's' para efetuar um sorteio ou qualquer outra tecla para sair: ")
    if sorteio.lower().strip() != 's':
        break
    while True:
        numero_sorteado = random.randint(1, 10)
        if numero_sorteado not in sorteados:
            sorteados.append(numero_sorteado)
            break
    print()
    print(f"O número sorteado foi: {numero_sorteado}")
    if numero_sorteado in cartela1:
        cartela1.remove(numero_sorteado)
        print(f"Cartela 1 pontuou! Falta: {cartela1}")
    if numero_sorteado in cartela2:
            cartela2.remove(numero_sorteado)
            print(f"Cartela 2 pontuou! Falta: {cartela2}")
    if numero_sorteado in cartela3:
            cartela3.remove(numero_sorteado)
            print(f"Cartela 3 pontuou! Falta: {cartela3}")
    if numero_sorteado in cartela4:
            cartela4.remove(numero_sorteado)
            print(f"Cartela 4 pontuou! Falta: {cartela4}")
    if numero_sorteado in cartela5:
            cartela5.remove(numero_sorteado)
            print(f"Cartela 5 pontuou! Falta: {cartela5}")
    if cartela1 == []:
        print("Bingo! Cartela 1 venceu!")
        vencedores.append("Cartela 1")
    if cartela2 == []:
        print("Bingo! Cartela 2 venceu!")
        vencedores.append("Cartela 2")
    if cartela3 == []:
        print("Bingo! Cartela 3 venceu!")
        vencedores.append("Cartela 3")
    if cartela4 == []:
        print("Bingo! Cartela 4 venceu!")
        vencedores.append("Cartela 4")
    if cartela5 == []:
        print("Bingo! Cartela 5 venceu!")
        vencedores.append("Cartela 5")
        
    if len(vencedores) >= 2:
        print("Houve empate entre as cartelas: " + ", ".join(vencedores))
        break
    if cartela1 == [] or cartela2 == [] or cartela3 == [] or cartela4 == [] or cartela5 == []:
        break