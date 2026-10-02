temperature = 75

if temperature < 0:
    print('Water is freezing')
elif temperature < 100:
    print('Water is not boiling ')
else:
    print('Water is boiling')


score = 50
present_exam = True

if score > 60 and present_exam:
    print('Probably aprove')
elif score == 50 and present_exam:
    print('Could aprove but have to study a lot')
else:
    print('No aprove')