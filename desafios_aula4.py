import random
# dic_compra_total = {}
# valor_total = 0

# def comprar(produto, quantidade, preco):
#     dic_compra_total[produto] = (quantidade, preco)

# while True:
#     produto = input("Digite o nome do produto (ou nada para finalizar a compra): ")
#     if not produto:
#         break
#     quantidade = int(input("Digite a quantidade: "))
#     if quantidade <= 0:
#         print("Quantidade inválida. Digite um valor maior que zero.")
#         continue
#     preco = float(input("Digite o preço unitário: "))
#     comprar(produto, quantidade, preco)
    
# for produto, (quantidade, preco) in dic_compra_total.items():
#     print(f"Produto: {produto}, Quantidade: {quantidade}, Preço unitário: R$ {preco:.2f}")

# for produto, (quantidade, preco) in dic_compra_total.items():
#     valor_total += quantidade * preco

# print(f"Valor total da compra: R$ {valor_total:.2f}") if dic_compra_total else print("Comprou nada.")

# ------------------------------------------------------------------

# populacao_paises = {
#     "Índia": 1428000000,
#     "China": 1425000000,
#     "Estados Unidos": 339000000,
#     "Indonésia": 277000000,
#     "Paquistão": 240000000,
#     "Nigéria": 223000000,
#     "Brasil": 216000000,
#     "Bangladesh": 173000000,
#     "Rússia": 144000000,
#     "México": 128000000,
# }

# pais = input("Digite o nome de um país: ")
# pais = pais.strip().title()
# if pais in populacao_paises:
#     print(f"A população do país '{pais}' é de {populacao_paises[pais]:,} habitantes!".replace(',', '.'))
# else:
#     print("País não encontrado.")

# valor = []
# while sum(valor) <= 100:
#     add = int(input("Digite um número: "))
#     valor.append(add)
# print(f"O valor total é: {sum(valor)} e os valores são: {valor}")

# Crie uma lista com 5 números usando a biblioteca random. 
# Usando um while, percorra a lista (com a ajuda de len()) e imprima apenas os
# números pares encontrados.

lista = []
for i in range(5):
    lista.append(random.randint(1, 100))
    
i = 0
while i < len(lista):
    if lista[i] %2 == 0:
        print(f"{lista[i]} é par!")
    else:
        print(f"{lista[i]} é ímpar!")
    i += 1