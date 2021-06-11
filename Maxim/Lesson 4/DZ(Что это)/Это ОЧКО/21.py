from random import choice as ch
import sqlite3

def create_list():
    """Создает список из доступных значений"""
    for x in range(1, 12):
        for i in range(0, 4):
            if i < 4:
                list_of_number_cards.append(x)


def register():
    """Регистрирует имя пользователя"""
    global player_1, player_2
    player_1 = input('Введите свое имя: ')
    player_2 = input('Введите свое имя: ')


def main_game():
    """Основная игра"""
    global points_player_1, points_player_2
    points_player_1 = 0
    points_player_2 = 0
    print('Напишите "1" - если вы хотите тянуть карту, или оставьте поле пустым если отказываетесь брать')
    while True:
        if points_player_1 < 21 and points_player_2 < 21:
            print(f'{player_1}, ваш ход!')
            answer = input()
            if answer == '1':
                a = ch(list_of_number_cards)
                list_of_number_cards.remove(a)
                points_player_1 += a
                print('У вас - ', points_player_1, 'очков')
            print(f'{player_2}, ваш ход!')
            answer = input()
            if answer == '1':
                a = ch(list_of_number_cards)
                list_of_number_cards.remove(a)
                points_player_2 += a
                print('У вас - ', points_player_2, 'очков')
        else:
            results()
            break


def results():
    global answer, scr
    """Подведение итогов и предложение переигровки"""
    if points_player_1 == 21:
        print(f'{player_1}, вы выиграли')
    elif points_player_1 < 21 and points_player_1 > points_player_2:
        print(f'{player_1}, вы выиграли')
    elif points_player_2 > 21 and points_player_1 < points_player_2:
        print(f'{player_1}, вы выиграли')
    else:
        print(f'{player_1}, вы проиграли')

    if points_player_2 == 21:
        print(f'{player_2}, вы выиграли')
    elif points_player_2 < 21 and points_player_2 > points_player_1:
        print(f'{player_2}, вы выиграли')
    elif points_player_1 > 21 and points_player_2 < points_player_1:
        print(f'{player_2}, вы выиграли')
    else:
        print(f'{player_2}, вы проиграли')
    scr = f'{points_player_1}/{points_player_2}'
    print(f'Соотношение очков первого игрока ко второму - {scr}')
    append_data_base()
    answer = input('Если хотите покинуть игру нажмите "q", если хотите снова сыграть оставьте поле пустым\n')


def regame():
    """Подготовка перезапуска"""
    create_list()
    main_game()


def append_data_base():
    db = 'players_database.db'
    data = (player_1, player_2, scr)
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute(f'INSERT INTO games (first_player, second_player, "scr_1/scr_2") VALUES {data}')
        conn.commit()


list_of_number_cards = []
answer = ''
register()
while True:
    if answer == 'q':
        break
    else:
        regame()
