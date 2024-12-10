my_dict = { "Даня" : 2003 , "Слава" : 1997 , "Павел" : 2010 }
print(my_dict)
print(my_dict.get("Даня"))
print(my_dict.get("Саша"))
my_dict.update ({ "Дима" : 1995,
                  "Лера" : 2002 })
print(my_dict)
a = my_dict.pop("Павел")
print(a)
print(my_dict)
my_set = {51,42,32,51,42,33}
print(my_set)
my_set.add(99)
my_set.add(88)
my_set.discard(32)
print(my_set)
