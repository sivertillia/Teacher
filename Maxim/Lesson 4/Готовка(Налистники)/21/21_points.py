import random
import os

def create_deck_of_cards():
    deck_of_cards = [1, 2, 3, 4, 6, 7, 8, 9, 10] * 4
    random.shuffle(deck_of_cards)
    return deck_of_cards

deck_of_cards = create_deck_of_cards()
deck = []
def add_card(deck_of_cards):
    deck.append(deck_of_cards[0])
    del deck_of_cards[0]
def win_lose():
    if sum(deck) > 21:
        print("Вы насобирали больше 21 очка вы проиграли")
    elif sum(deck) == 21:
        print("Вы насобирали 21 очко вы выйграли")
    else:
        print(f"Вы насобирали {sum(deck)} очков!")
    exit()
def game():
    os.system('cls')
    print(deck, sum(deck))
    if sum(deck) > 21:
            win_lose()
    move = int(input("1. Брать\n2. Пас\n"))
    if move == 1:
        add_card(deck_of_cards)
    else:
        win_lose()

for i in range(2):
    add_card(deck_of_cards)
while 1:
    game()