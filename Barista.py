recepts = {'Эспрессо': [1, 0, 0],
           'Капучино': [1, 3, 0],
           'Маккиато': [2, 1, 0],
           'Кофе по-венски': [1, 0, 2],
           'Латте Маккиато': [1, 2, 1],
           'Кон Панна': [1, 0, 1]
           }


def choose_coffee(preferences):
    for i in preferences:
        if recepts[i][0] <= ingredients[0] and recepts[i][1] <= ingredients[1] \
                and recepts[i][2] <= ingredients[2]:
            ingredients[0] -= recepts[i][0]
            ingredients[1] -= recepts[i][1]
            ingredients[2] -= recepts[i][2]
            print(i)
        else:
            print('К сожалению, не можем предложить Вам напиток')


ingredients = [4, 4, 0]
choose_coffee('Капучино, Маккиато, Эспрессо'.split(', '))

