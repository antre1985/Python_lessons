def season(m):
    if m < 1:
        return "Да я смотрю ты гений?!"
    if m == 12 or m < 3:
        return "Зима"
    if 2 < m < 6:
        return "Весна"
    if 5 < m < 9:
        return "Лето"
    if 8 < m < 12:
        return "Осень"

m = int(input("Введите номер месяца: "))
print(season(m))