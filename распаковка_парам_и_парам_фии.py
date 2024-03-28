def print_params(a = 1, b = 'строка', c = True):
    print(a, b)
    print(a, b, c)
    print(c, c, c)
    print()



print_params(c = [1, 2, 3])
print_params(b = 25)

############################################

values_list = ['apple', 12.50, False]
values_dict = {'a': 15, 'b': 'столбец', 'c': None}

print_params(**values_dict)
print_params(*values_list)

############################################

values_list_2 = ['juice', 57]

print_params(*values_list_2, 42)