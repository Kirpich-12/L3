from math import pi, sqrt, sin
# Имопрь нужных функций

rad = int(input('Добрый день! Введите радиус интересующего вас круга '))
#Взять значения радиуса

C = 2 * pi * rad #длинна окружности
S = 2 * (pi * pi) #площадь окружности 


st_k = sqrt(S) # сторона вписанного квдрата
st_tr = rad * sqrt(3) # сторона вписанного треугольника

st_k_op = rad * 2 # сторона описанного квадрата 
st_tr_op = rad * 2 * sqrt(3) # сторона описанного треугольника 
st_vsm = rad * 2 * sin(180/8) # сторона описанного восьмиугольника


print('Длинна окружности:', C,'В метрах', C/100, '\n'
       'Площадь круга:', S, 'В метрах: ', S/100, '\n', 
       'Сторона вписанного квадрата:', st_k, '\n', 'Сторона вписанного треугольника', st_tr, '\n', 'сторона описанного квадртата', st_k_op, '\n',  'сторона описанного треугольника', st_tr_op, '\n',  'сторона описанного восьмиугольника', st_vsm )
# Вывод в дружественном интерфейсе всего полученного 






