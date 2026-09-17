# filmes = [
#     "Crepúsculo dos Deuses",
#     "A Malvada",
#     "Um Lugar ao Sol",
#     "O Maior Espetáculo da Terra",
#     "Nasce uma Estrela",
#     "Ladrão de Casaca",
#     "A Volta ao Mundo em 80 Dias",
#     "A Ponte do Rio Kwai",
#     "Um Corpo que Cai",
#     "Ben-Hur",
#     "Psicose",
#     "Amor, Sublime Amor",
#     "Lawrence da Arábia",
#     "O Sol É para Todos",
#     "Música no Coração",
#     "Doutor Jivago",
#     "O Bom, o Mau e o Feio",
#     "A Primeira Noite de um Homem",
#     "2001: Uma Odisseia no Espaço",
#     "Butch Cassidy",
#     "Patton - Rebelde ou Herói?",
#     "Operação França",
#     "O Poderoso Chefão",
#     "O Exorcista",
#     "O Poderoso Chefão - Parte II",
#     "Um Estranho no Ninho",
#     "Rocky, um Lutador",
#     "Star Wars: Episódio IV - Uma Nova Esperança",
#     "O Franco Atirador",
#     "Kramer vs. Kramer",
#     "Touro Indomável",
#     "Carruagens de Fogo",
#     "E.T. - O Extraterrestre",
#     "Star Wars: Episódio VI - O Retorno do Jedi",
#     "O Exterminador do Futuro",
#     "De Volta para o Futuro",
#     "Platoon",
#     "Os Intocáveis",
#     "Rain Man",
#     "Nascido em 4 de Julho",
#     "Dança com Lobos",
#     "O Silêncio dos Inocentes",
#     "Os Imperdoáveis",
#     "A Lista de Schindler",
#     "Forrest Gump",
#     "Coração Valente",
#     "O Paciente Inglês",
#     "Titanic",
#     "Shakespeare Apaixonado",
#     "Beleza Americana",
#     "Gladiador",
#     "Uma Mente Brilhante",
#     "Chicago",
#     "O Senhor dos Anéis: O Retorno do Rei",
#     "Menina de Ouro",
#     "Crash - No Limite",
#     "Os Infiltrados",
#     "Onde os Fracos Não Têm Vez",
#     "Quem Quer Ser um Milionário?",
#     "Guerra ao Terror",
#     "O Discurso do Rei"
# ]

# ano = int(input("Digite o ano em que você nasceu: "))

# if 1950 <= ano <= 2010:
#     print(f"O filme do seu ano de nascimento é: {filmes[ano - 1950]}")
# else:
#     print("O ano precisa estar entre 1950 e 2010.")

# tupla = 11,22,51,86,12,71,63
# m = 0
# for i in tupla:
#     i = int(i)
#     m += i
    
# print(f"A média da lista é {m/len(tupla)}")

# while True:
#     v1 = int(input("Digite o primeiro valor: "))
#     v2 = int(input("Digite o segundo valor: "))
#     op = input("Digite '+' para soma, '-' para subtração, '*' para multiplicação e '/' para divisão: ")
    
#     if op == "+":
#         print(f"A soma de {v1} com {v2} é {v1+v2}")
#     elif op == "-":
#         print(f"A subtração de {v1} por {v2} é {v1-v2}")
#     elif op == "*":
#         print(f"A multiplicação de {v1} e {v2} é {v1*v2}")
#     elif op == "/":
#         if v2 == 0:
#             print(f"Não existe divisão por 0!")
#         else:    
#             print(f"A divisão de {v1} por {v2} é {round(v1/v2, 2)}")
#     else: 
#         print("Comando não encontrado")
    
#     cont = input("Digite 's' para repetir ou qualquer outra tecla para sair: ")
#     if cont.lower().strip() != "s":
#         break

# def calcular_velocidade_media(d, t):
#     if t <= 0:
#         return "O tempo deve ser maior que zero."
#     velocidade_media = d / t
#     return round(velocidade_media, 2)

# distancia = float(input("Digite a distância percorrida (em km): "))
# tempo = float(input("Digite o tempo gasto (em horas): "))
# velocidade_media = calcular_velocidade_media(distancia, tempo)
# print(f"A velocidade média é: {velocidade_media} km/h")

multiplo = int(input("Digite um número para definir o múltiplo do jogo do pin: "))
limite = int(input("Digite um número para definir o limite do jogo do pin: "))
resultado = []
i = 0

while i < limite:
    i += 1
    if i % multiplo == 0:
        resultado.append('pin')
    else:
        resultado.append(i)
        
print(resultado)
