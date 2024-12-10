immutable_var = 1, 2, 3
print(immutable_var)
#immutable_var[0] = 13       кортеж не поддерживает обращение по элементам

mutable_list = ([1,23],45, True)
mutable_list[0][0] = 52
print(mutable_list)
