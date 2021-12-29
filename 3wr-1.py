def div(*args):

    try:
        arg1 = int(input("Аргумент первый "))
        arg2 = int(input("Аргумент второй "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Wrong devider! You can't use zero as a devider"

    return res

    '''
    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Wrong number! Devider can't be null")
    '''


print(f'result  {div()}')