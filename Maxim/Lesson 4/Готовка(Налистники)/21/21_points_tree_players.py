from random import shuffle
import os

players = []
deck = [[],[],[]]

def create_deck_of_cards():
    deck_of_cards = [1, 2, 3, 4, 6, 7, 8, 9, 10] * 4
    shuffle(deck_of_cards)
    return deck_of_cards

deck_of_cards = create_deck_of_cards()

for i in range(3):
    player = input("Name: ")
    players.append(player)

def add_card(name):
    if name == players[0]:
        deck[0].append(deck_of_cards[0])
        del deck_of_cards[0]
    if name == players[1]:
        deck[1].append(deck_of_cards[0])
        del deck_of_cards[0]
    if name == players[2]:
        deck[2].append(deck_of_cards[0])
        del deck_of_cards[0]

def game():    
    print("1. Брать\n0. Пас")
    while True:
        move = 0
        if sum(deck[0]==21 or deck[1]==21 or deck[2]==21):
            move = int(input(f"{players[0]}, ходит: "))
            if move == 1:
                add_card(players[0])
                print(deck[0], sum(deck[0]))
            move = int(input(f"{players[1]}, ходит: "))
            if move == 1:
                add_card(players[1])
                print(deck[1], sum(deck[1]))
            move = int(input(f"{players[2]}, ходит: "))
            if move == 1:
                add_card(players[2])
                print(deck[2], sum(deck[2]))



for i in range(2):
    add_card(players[0])
    add_card(players[1])
    add_card(players[2])
        
print(deck)
game()
