a = 10


while a >= 0:
    print(a)
    a -= 1
    if a < 0:
        print('While loop end \n\n')


for i in range(0,10):
    print(i)
    if i == 9:
        print('For loop using range ends \n\n')


for i in range(0,10,2):
    print(i)
    if i == 9:
        print('For loop using range and count by 2 ends \n\n')
