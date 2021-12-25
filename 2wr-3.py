
season_list = ['зима', 'весна', 'лето', 'осень']
season_dict = {1 : 'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}
month = int(input("Введите месяц по номеру "))
if month == 1 or month == 2 or month == 12:
    print(season_dict.get(1))
if month == 3 or month == 4 or month == 5:
    print(season_dict.get(2))
if month == 6 or month == 7 or month == 8:
    print(season_dict.get(3))
if month == 9 or month == 10 or month ==11:
    print(season_dict.get(4))
else:
    print('Такого месяца не существует')

