my_list = 1
my_list_1 = "Hello"
my_list_2 = 1.3
my_list_3 = True
my_list_4 = None
my_list_5 = [2, 3]
my_list_6 = (2, 3.5, list)
my_list_7 = {'key_1': 'val_1', 'key_2': 'val_2'}
my_list_8 = {400, True, None}
for ind, el in enumerate(['my_list', 'my_list_1', 'my_list_2', 'my_list_3', 'my_list_4', 'my_list_5','my_list_6']):
    print(f"{ind}) {el} - {type(el)}")