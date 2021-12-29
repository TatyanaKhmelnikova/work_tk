def x_pow (x, y):
    try:
        x, y = float(x), int(y)
        if x >= 0 or y <= 0:
            return 'Ошибка: x должен быть больше 0, а y меньше нуля'
        else:
            result = 1
            for _ in range(abs(y)):
                result *= 1 / x
                return f'Результат возведения в степень y {round(result, 6)}'


print(x_pow(3, -2))

