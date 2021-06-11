number = input("Введите число: ")
try:
    number = int(number)
    days = number // (24 * 3600)
    number = number % (24 * 3600)
    hours = number // 3600
    number = number % 3600
    minute = number // 60
    number = number % 60
    sec = number % 60
    print(f"{days}:{hours}:{minute}:{sec}")
except ValueError:
    print("Вы ввели не число")