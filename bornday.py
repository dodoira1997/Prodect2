birth = int(input('Какой год рождения у А.С.Пушкина?'))
if birth != 1799:
    print('Неверный год')
else:
    dr = int(input('Назовите день рождения Пушкина?'))
    print(dr)
    if dr==6:
        print('Верно')
    else:
        print('Неверный день рождения')
