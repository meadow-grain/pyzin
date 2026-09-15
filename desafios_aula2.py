# nota1 = input("Digite a primeira nota: ")
# nota1 = float(nota1)
# peso1 = input("Digite o peso da primeira nota: ")
# peso1 = float(peso1)
# nota2 = input("Digite a segunda nota: ")
# nota2 = float(nota2)
# peso2 = input("Digite o peso da segunda nota: ")
# peso2 = float(peso2)
# m_pon = (nota1*peso1+nota2*peso2)/(peso1+peso2)
# print('A média ponderada das notas é:',m_pon)

# cap = input("Digite o capital investido: ")
# cap = float(cap)
# tx = input("Digite a taxa de juros (em %): ")
# tx = float(tx)
# tempo = input("Digite o tempo de aplicação (em meses): ")
# tempo = int(tempo)
# juros = cap * (tx/100) * tempo
# montante = cap + juros
# parcelas = montante / tempo
# print('O montante final após',tempo,'meses, na taxa de',tx,'será de: R$',montante)
# print('O valor de cada parcela será de: R$',parcelas)

# emprestimo = input("Digite o valor do empréstimo: ")
# emprestimo = float(emprestimo)
# taxa = input("Digite a taxa de juros simples (em %): ")
# taxa = float(taxa)
# tempo_emprestimo = input("Digite o tempo do empréstimo (em meses): ")
# tempo_emprestimo = int(tempo_emprestimo)
# juros_emprestimo = emprestimo * (taxa/100) * tempo_emprestimo
# montante_emprestimo = emprestimo + juros_emprestimo
# parcelas_emprestimo = montante_emprestimo / tempo_emprestimo
# print('O montante final do empréstimo após',tempo_emprestimo,'meses, na taxa de',taxa,'será de: R$',montante_emprestimo)
# print('O valor de cada parcela será de: R$',parcelas_emprestimo)

# medida = input("Digite a medida: ")
# medida = float(medida)
# while True:
#     conversao = input("Digite 'cm' para converter m para cm ou 'm' para converter cm para m: ")
#     if conversao == 'cm':
#         print(f"{medida} metro(s) em centímetros é: {medida * 100}")
#         break
#     elif conversao == 'm':
#         print(f"{medida} centímetro(s) em metros é: {medida / 100}")
#         break
#     else: 
#         print("Opção inválida. Por favor, digite 'cm' ou 'm'.")
#         continue

# planta = input("Digite o nome da planta: ")
# sementes, flores, reproducao, frutos, vasos = "", "", "", "", ""
# sementes = input("A planta produz sementes? (s/n): ")
# flores = input("A planta produz flores? (s/n): ")
# reproducao = input("A planta depende de água para fecundação? (s/n): ")
# frutos = input("A planta produz frutos? (s/n): ")
# vasos = input("A planta possui vasos condutores? (s/n): ")

# if sementes == "s" and flores == "s" and reproducao == "n" and frutos == "s" and vasos == "s":
#     print(f"A planta {planta} é uma Angiosperma.")
# elif sementes == "s" and flores == "s" and reproducao == "n" and frutos == "n" and vasos == "s":
#     print(f"A planta {planta} é uma Gimnosperma.")
# elif sementes == "n" and flores == "n" and reproducao == "s" and frutos == "n" and vasos == "s":
#     print(f"A planta {planta} é uma Pteridófita.")
# elif sementes == "n" and flores == "n" and reproducao == "s" and frutos == "n" and vasos == "n":
#     print(f"A planta {planta} é uma Briófita.")
# else: 
#     print(f"A planta {planta} não se enquadra em nenhuma das categorias conhecidas, ou você respondeu de forma inconsistente.")

# valor_renda = round(float(input("Digite o valor da renda em reais: ")), 2)

# if valor_renda <= 1903.98:
#     print("Não paga imposto de renda.")
# elif valor_renda > 1903.98 and valor_renda <= 2826.65:
#         print("Você vai pagar 7,5% de imposto de renda.")
# elif valor_renda > 2826.65 and valor_renda <= 3751.05:
#         print("Você vai pagar 15% de imposto de renda.")
# elif valor_renda > 3751.05 and valor_renda <= 4664.68:
#         print("Você vai pagar 22,5% de imposto de renda.")
# else:
#         print("Se lascou. Você vai pagar 27,5% de imposto de renda.")
        
# linguagens = ['Java', 'PHP', 'C', 'Ruby']
# linguagens[linguagens.index('Java')] = 'Python'
# linguagens.append('JavaScript')
# linguagens.remove('PHP')
# print(linguagens)

# frutas = ['banana', 'maçã', 'uva', 'manga']
# nova = input("Digite uma fruta para adicionar à lista: ")
# if nova not in frutas:
#     frutas.append(nova)
# frutas[frutas.index('uva')] = 'morango'
# if len(frutas) > 4:
#     frutas.pop(0)
# print(frutas)

# nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))
# priori = input("Você é gestante ou possui alguma deficiência? (s/n): ")

# if idade < 60 or priori == 's':
#     print("Atendimento prioritário")
# else:
#     print("Fila normal")

convidados = ['Ana', 'Bruno', 'Carla', 'Diego']
checar = input("Digite o nome do convidado para verificar se está na lista: ")
if checar in convidados:
    print(checar, "foi confirmado para a festa.")
    convidados.remove(checar)
else:
    print("Confirmação adicionada")
    convidados.append(checar)
print("Lista atualizada de convidados:", convidados)