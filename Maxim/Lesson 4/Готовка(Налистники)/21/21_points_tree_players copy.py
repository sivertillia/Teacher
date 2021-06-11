import random
import os

deck = []

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