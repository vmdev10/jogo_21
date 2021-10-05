import random

print('''
                        VINTE E UM
O objetivo do jogo é completar a soma de 21 pontos com as cartas, ou chegar o mais próximo possível
sem ultrapassar esse valor. As cartas numéricas tem o valor do número nela presente.
Valete (J), Dama (Q) e Reis (K) valem 10. O ás vale 1.
''')

deck_cards_numbers = ['A', 1, 2, 3, 4, 5, 6, 7, 8, 9,
                      10, 'J', 'Q', 'K']
deck_cards_simbols = ['♥', '♦', '♣', '♠']

try_again = 'SIM'

while (try_again == 'SIM'):
    name = input('Nome do jogador: ')
    new_card = 'SIM'
    score_player = 0
    score_computer = 0

    while new_card == 'SIM':

        card_value = random.choice(deck_cards_numbers)
        card_simbol = random.choice(deck_cards_simbols)

        print(f'''
            {name}, sua carta é:
            _______________
            |               |
            |           {card_value} {card_simbol}
            |               |
            |               |
            |               |
            |               |
            |               |
            ---------------
    '''
              )

        if (card_value == 'A'):
            card_value = 1
        elif (card_value == 'J' or card_value == 'Q' or card_value == 'K'):
            card_value = 10

        score_player = score_player + card_value

        print(
            f'                                                             {name}, seu score é de: {score_player}')

        card_value = random.choice(deck_cards_numbers)
        card_simbol = random.choice(deck_cards_simbols)

        print(f'''
            Adverdsário, sua carta é:
            _______________
            |               |
            |           {card_value} {card_simbol}
            |               |
            |               |
            |               |
            |               |
            |               |
            ---------------
    '''
              )

        if (card_value == 'A'):
            card_value = 1
        elif (card_value == 'J' or card_value == 'Q' or card_value == 'K'):
            card_value = 10

        score_computer = score_computer + card_value

        print(
            f'                                                             Adverśario, seu score é de: {score_computer}')

        if(score_player > 21):
            print('Você perdeu!')
            break
        elif (score_computer > 21):
            print('Você venceu!!!')
            break

        new_card = input('Deseja pegar mais uma carta? Sim ou não? ').upper()

        if(new_card == 'NÃO' or new_card == 'NAO'):
            if (score_player < score_computer):
                print('Você venceu!!')
            else:
                print('Você perdeu!!')

    try_again = input('Jogar novamente? Sim ou não? ').upper()
