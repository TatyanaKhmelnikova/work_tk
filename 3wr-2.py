name = input('enter name')
surname = input('enter surname')
year = input('enter year')
city = input('enter city')
email = input('enter email')
telephone = input('input telephone')

def my_func (name, surname, year, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])
print(my_func(surname = 'Khmelnikova', name = 'Tatyana', year = '1988', city = 'Saint Petersburg', email = 'propan_212015@mail.ru', telephone = '8-911-745-39-29'))