def say_hello() -> str:
    print ('Hi and welcome to my function')

say_hello()


def water_status(temperature) -> str:
    if temperature < 0:
        return 'Water is freezing'
    elif temperature < 100:
        return 'Water is not boiling '
    else:
        return 'Water is boiling'

print(water_status(-25))
print(water_status(62))
print(water_status(150))

def calculate_discount(price, member, discount):
    if not member:
        print(f'Original price: {price} \n'
              f'Total discount: {price*(discount/100)} \n'
              f'New price: {price*(100-discount)/100} \n')
    else:
        discount = 50
        print(f'Original price: {price} \n'
              f'Total discount: {price*(discount/100)} \n'
              f'New price: {price*(100-discount)/100} \n')

calculate_discount(100, True, 20)

global_var = 'Hi i\' a global variable'

def look_var():
    global_var = 'Hi i\' a local variable named global_var'
    print(global_var)

look_var()
print(global_var)