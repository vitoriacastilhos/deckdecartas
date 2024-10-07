import time

def pseudo_random(seed, i):
    # Usa o tempo como semente, misturado com o índice i para criar um número "aleatório"
    return (seed + i * 31) % 52  # Modulo para garantir que o número fique dentro do range do deck

def criar_deck():
    naipes = ['♥', '♦', '♣', '♠']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [f'{valor}{naipe}' for naipe in naipes for valor in valores]
    return deck

def fisher_yates_shuffle(deck):
    n = len(deck) #52
    seed = int(str(time.time_ns())[-6:])  # Últimos 6 dígitos do tempo em nanossegundos como semente

    # Percorrendo o deck de trás para frente
    for i in range(n-1, 0, -1):
        # Gerar índice "aleatório" usando a função pseudo_random
        j = pseudo_random(seed, i) % (i + 1)  # Gera um índice entre 0 e i
        # Trocar os elementos nas posições i e j
        deck[i], deck[j] = deck[j], deck[i]
    
    return deck

def distribuir_cartas(deck, quantidade):
    if quantidade > len(deck):
        return "Não há cartas suficientes no deck!"
    cartas_distribuidas = deck[:quantidade]
    deck = deck[quantidade:]  # Remove as cartas distribuídas do baralho
    return cartas_distribuidas, deck

deck = criar_deck()  # Criar o deck de 52 cartas
deck_embaralhado = fisher_yates_shuffle(deck)

qte_cartas = int(input("\nDigite a quantidade de cartas a ser distribuída: "))
cartas_distribuidas, deck_restante = distribuir_cartas(deck_embaralhado, qte_cartas)
print("\nCartas distribuídas:")
print(cartas_distribuidas)

print("\n1. Mostrar deck original")
print("2. Mostrar deck embaralhado")
print("3. Mostrar deck restante")

opcao = input("Digite a opção desejada: ")

if opcao == '1':
    print("\nDeck original:")
    print(deck)

elif opcao == '2':
    print("\nDeck embaralhado:")
    print(deck_embaralhado)

elif opcao == '3':
    print("\nDeck restante:")
    print(deck_restante)

else:
    print("Opção inválida")