def print_params (a = 1, b = 'строка', c = True):
    print (a, b, c)

print_params()
print_params (b = 25)
print_params (c = [1, 2, 3])
values_list = (2, 'буква', False)
print_params (*values_list)
values_dict = {'a': 1, 'b': 'строка', 'c': True}
print_params (*values_dict.items ())
values_list_2 = (4.5, 'строка')
print_params (*values_list_2)
print_params(*values_list_2, 42)
