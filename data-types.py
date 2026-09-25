# Numbers
a_number = 215
print(a_number)
print(f'I\'m a {type(a_number)}')

a_float = 3.1415
print(a_float)
print(f'I\'m a {type(a_float)}')

suma = a_number + a_number
resta = a_number - a_float
multi = a_number * 5
div = a_number / 5
div_entera = a_number // 5
pot = a_float ** 2

print(suma, resta, multi, div, div_entera, pot)

# Strigs
a_string = 'Hello World!'
print(a_string)
print(f'I\'m a {type(a_string)}')

also_string = '215'
print(also_string)
print(f'I\'m a {type(also_string)}')

character = 'a'
print(character)
print(f'I\'m a {type(character)}')

concat_1 = a_string + ' ' + also_string
concat_2 = f'{a_string} {also_string}'

long_dash = '-' * 30
print(long_dash)

print (concat_1,'\n',concat_2)

# Boolean

true = True
print(true)
print(f'I\'m a {type(true)}')

false = False
print(false)
print(f'I\'m a {type(false)}')

print(true and false)
print(true or false)
print(not false)
print(1 == 2)
print(1 < 2)
print(1 >= 2)
print(true == 1)

