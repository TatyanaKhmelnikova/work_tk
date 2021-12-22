while True:
    days = 1
    day_1 = float(input("Результат 1-го дня, км: "))
    day_n = float(input("Результат n-го дня, км: "))
    if day_1 <= 0 or day_n < 0:
        print("Результат должен быть больше нуля!")
    else:
        while day_1 < day_n:
            day_1 = int(day_1+(day_1*0.1))
            day_n =+ 1
        print(f"Спортсмен добьется результата за {day_n} дней")




