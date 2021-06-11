try:
    number = int(input("Введите число: "))
    time_sec_test = {"days": (24*3600),"hours": 3600,"min": 60,"sec": 60}
    for i in time_sec_test:
        if i != "sec":
            time = number // time_sec_test[i]
            time_sec_test[i] = number % time_sec_test[i]
        else: time = number % time_sec_test[i]
        print(f"{time} {i} ", end="")
except ValueError:
    print("Вы ввели не число")