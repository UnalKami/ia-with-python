# Lists

a_list = [1,2,3,4,5,6,7,8,9]
b_list = ['a','b','c','d','e']

variable = 3.058

c_list = ['Alice', 20, variable, True]

print(a_list)
print(b_list)
print(c_list)

one_element = a_list[5]
print(one_element)

fruits_list = ['apple', 'pear', 'grapes']
print(f'Base list: {fruits_list}')
new_fruit = 'orange'


fruits_list.append(new_fruit)
print(f'New list before append an orange: {fruits_list}')

fruits_list.insert(1,'Kiwi')
print(f'New list before insert a Kiwi in index 1: {fruits_list}')

fruits_list.remove('pear')
print(f'New list before remove pear: {fruits_list}')

print(f'Last fruit in fruits_list is: {fruits_list.pop()} \n'
      f'And now it no more in fruits_list, look: {fruits_list}')


print('\n \n')


# Dictionaries

my_dict = {}

my_profile = {
    'name': 'Camilo',
    'age': 25,
    'born': '02-09-2001',
    'engineer': True
}

print(my_profile)

print(f'Name in my profile {my_profile['name']}')

print('We can add a new key-value in the dictionarie')
my_profile['have_cat'] = True

print(my_profile)

del my_profile['born']
print('Dictionarie before delete born key')
print(my_profile)


print('\n \n')


# Tuples
empty_tuple = ()

names_tuple = ('Juan','Mateo','Antonio','Maria','Oscar')

print(names_tuple[0])
print(names_tuple[-1])
print(names_tuple[1:3])


## Sets
empty_set = set()

set_numbers = {1,2,3,4,5}
set_letters = set(b_list)

print(set_numbers)
print(set_letters)

scores = [90,60,98,90,73,56,60,60,57,14]
set_scores = set(scores)
print(set_scores)

set_scores.add(65)
print(set_scores)

set_scores.remove(90)
print(set_scores)

set_scores.discard(60)
print(set_scores)
