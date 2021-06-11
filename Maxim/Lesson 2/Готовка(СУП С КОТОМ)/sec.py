
def time(sec):
    days = sec // (24 * 3600)
    sec = sec % (24 * 3600)
    hours = sec // 3600
    sec = sec % 3600
    minu = sec // 60
    sec = sec % 60
    sec = sec % 60
    print(f"{days}:{hours}:{minu}:{sec}")

time(123456789)