from operator import truediv


def print_params(a = 1, b = "строка", c = True):
    print(a, b ,c)

print_params()
print_params(b =25)
print_params(c = [1,2,3])
print('________________________________________')

values_list = ("мост",True,5)
values_dict = {'a': 5, 'b': False, 'c' : 'штраф поап'}
print_params(*values_list)
print_params(**values_dict)
values_list2 = (1, True)
print_params(*values_list2,42)