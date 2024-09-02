# Словари и множества
my_dict = {'Den' : 1956, 'Ksy' : 2001, 'Max' : 1578}
print(my_dict)
print(my_dict['Den'])
my_dict.update({'And' : 2002,
                      'Kris' : 1978})
b = my_dict.pop('And')
print(b)
print(my_dict.get('Sara'))
print(my_dict)
# множества
my_set = {1, 1, 2, 4, 2, 3}
print(my_set)
my_set.add('Rus')
my_set.add('Rum')
my_set.remove(3)
print(my_set)