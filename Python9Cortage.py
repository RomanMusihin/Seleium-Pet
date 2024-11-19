data = (4, 6, 9, 2, 4, 0)
# print(data[1:5])

#tuple (кортеж) - это неизменяемы список
cortage = 4, 6, 2, True
cortage2 = (5,)

#for i in cortage:
    # print(i)

list = [4, 6, 9]
list_to_tuple = tuple(list)
print(list_to_tuple)



color1, color2 = input(), input()
if (color1 == 'красный' and color2 == 'синий') or (color2 == 'красный' and color1 == 'синий'):
    print('фиолетовый')
elif (color1 == 'красный' and color2 == 'желтый') or (color2 == 'красный' and color1 == 'желтый'):
    print('оранжевый')
elif (color1 == 'синий' and color2 == 'желтый') or (color2 == 'синий' and color1 == 'желтый'):
    print('зеленый')
elif color1 == color2 == 'красный' or color1 == color2 == 'синий' or color1 == color2 == 'желтый':
    print(color1)
else:
    print('ошибка цвета')


color1, color2 = input(), input()
if color1 == 'красный':
    if color2 == 'желтый':
        print('оранжевый')
    elif color2 == 'синий':
        print('фиолетовый')
elif color1 == 'желтый':
    if color2 == 'красный':
        print('оранжевый')
    elif color2 == 'синий':
        print('зеленый')
elif color1 == 'синий':
    if color2 == 'красный':
        print('фиолетовый')
    elif color2 == 'желтый':
        print('зеленый')
else:
    print('ошибка цвета')




n = int(input())
if n == 0:
    print('зеленый')
elif 1 <= n <= 10 or 19 <= n <= 28:
    if n % 2 == 0:
        print ('черный')
    else:
        print('красный')
elif 11 <= n <= 18 or 29 <= n <= 36:
    if n % 2 == 0:
        print ('красный')
    else:
        print('черный')
else:
    print('ошибка ввода')