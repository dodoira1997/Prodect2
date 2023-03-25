balls = 0
minus = 0

while True:
    #год рождения 1834
    birth = int(input('Какой год рождения у Менделева Д.И.?'))
    if birth == 1834:
        print('Верно')
        balls += 1
    else:
        print('Неверно')
        minus += 1
    # год рождения 1711
    birth = int(input('Какой год рождения у Ломоносова М.В.?'))
    if birth == 1711:
        print('Верно')
        balls += 1
    else:
        print('Неверно')
        minus += 1
        # год рождения 1863
    birth = int(input('Какой год рождения у Вернадского В.И.?'))
    if birth == 1863:
        print('Верно')
        balls += 1
    else:
        print('Неверно')
        minus += 1
        # год рождения 1707
    birth = int(input('Какой год рождения у Карла Линнея?'))
    if birth == 1707:
        print('Верно')
        balls += 1
    else:
        print('Неверно')
        minus += 1
        # год рождения 1904
    birth = int(input('Какой год рождения у Павлова И.П.?'))
    if birth == 1904:
        print('Верно')
        balls += 1
    else:
        print('Неверно')
        minus += 1
    zan = (input('Хотите ли начать векторину занова?'))
    if zan == 'Да':
        print('Продолжаем')
    elif zan!= 'Да':
        break
print(f'Количество верных ответов: {balls}')
print(f'Количество неверных ответов: {minus}')
print(f'Процент верных ответов: {balls*100/5}')
print(f'Процент неверных ответов: {minus*100/5}')

