from pprint import pprint

def receipt_read(receipt): # функция читает из файла рецепт и складывает в словарь определенным образом
    Ing = [] #список для хранения ингредиентов/ веса / измеряемой величины
    CookBook = {} #Итоговый словарь

    with open(receipt) as r:
        while True:
            dish_list = [] #инициация списка для хранения вложенных словарей по блюду
            dish_name = r.readline().rstrip() # название блюда
            #        print(dish_name)
            NumIngredients = r.readline().rstrip() #количество ингредиентов
            #        print(NumIngredients)
            if not dish_name and not NumIngredients: #прерывание цикла while
                break
            #   Здесь поднимается ошибка Value Error если использовать генератор списков вместо цикла далее внутри TRY,
            #   и разобраться с этим не получилось// ПЛИЗ ХЕЛП, где косяк?
            #        Ing = [r.readline().rstrip() for Ingredient in range(int(NumIngredients))]
            #        print(Ing)
            try:
                for Ingredient in range(int(NumIngredients)): #обработчик  ингредиентов с преобразованием в словари
                    Ingredient = r.readline().rstrip()
                    #                print(Ingredient)
                    Ing = Ingredient.split(' | ')
                    Ing_dict = {"Ingredient":Ing[0],"quantity":int(Ing[1]),"мeasure":Ing[2]}
                    dish_list.append(Ing_dict)
            except ValueError:
                print('Ошибка была (либо неверный формат ввода данных, либо ошибка в количестве ингредиентов')
            #        pprint(dish_list)
            CookBook.update({dish_name:dish_list}) #формирование итогового словаря
            r.readline()
        return CookBook
# Загрузка результата работы функции в словарь, для обработки заданием №2 # не разобрался, как это сделать из Main()
CookBook = receipt_read('receipt.txt')

#pprint(CookBook)
#пока не обернут в функцию - вычисление ингредиентов

def To_cook(ToCook,person):
    person = int(person)
    DishTmp = str
    ToCookTmp = []

    i = 0
    ingridients_for_dish = {} #Итоговый словарь, по идее
    temp = {}
#    ToCook = ['Каша из Топора','Омлет','Попеченный картофель','Попеченный картофель 2'] #задание блюд для вычислений

    try:
        for DishToCook in ToCook: # Добавлена проверка дублирования
            if DishToCook == DishTmp:
                person *= 2
            else:
                ToCookTmp.append(DishToCook)
            DishTmp = DishToCook
        ToCook = ToCookTmp
#        print (ToCook)
        for DishToCook in ToCook: # Для блюд, которые выбраны для заказа
            for ingred in CookBook[DishToCook]: # ингредиенты для каждого блюда
                new_ingridient_for_dish = ingred #загружаю в новый временный словарь
                new_ingridient_for_dish['quantity'] *= person  #умножаю кол-во в соотв с персонами

                if new_ingridient_for_dish['Ingredient'] not in ingridients_for_dish: # Если в итоговом списке нет ингредиента
                    final_ingred = new_ingridient_for_dish.get('Ingredient') #Для финального словаря заголовок ингредиента
                    del new_ingridient_for_dish['Ingredient'] #Удаление из временного словаря ключа "Ингредиент"
                    temp = {final_ingred:new_ingridient_for_dish}  # Еще один временный словарь
                    ingridients_for_dish.update(temp) #Обноваление итогового словаря
                else:
                    quamtity = new_ingridient_for_dish ['quantity'] #если ингредиент повторяется
                    final_ingred = new_ingridient_for_dish.get('Ingredient')
                    ingridients_for_dish[final_ingred]['quantity'] += new_ingridient_for_dish ['quantity'] #то суммирую кол-во
        pprint(ingridients_for_dish)


    except KeyError:
        print('отсутсвующее или неверно-введенное блюдо')
        pass


def main():  # обработчик команд
    while True:
        user_input = input('Чтение рецептов (r) или список продуктов для блюд (d). ДЛя выхода q ')
        if user_input.lower() == 'd':
            To_cook(['Каша из Топора','Омлет','Попеченный картофель','Попеченный картофель'],3)

        if user_input.lower() == 'r':
            CookBook = receipt_read('receipt.txt')
            pprint(CookBook)
        elif user_input == 'q':
            print('bye')
            break

def teacher_function():
    with open('receips.txt') as f:
        cook_book = {}
        for line in f:
            name_dishes = line.strip()
            amount_ingredients = int(f.readline().strip())
            ingredients_list = []
            while amount_ingredients != 0:
                ingredients = f.readline().strip().split('|')
                ingredients_dict = {'ingredient_name': ingredients[0], 'quantity': ingredients[1], 'measure': ingredients[2]}
                amount_ingredients -= 1
                ingredients_list.append(ingredients_dict)
            f.readline().strip()
            cook_book_new = {name_dishes: ingredients_list}
            cook_book.update(cook_book_new)

#To_cook(['Каша из Топора','Омлет','Попеченный картофель','Попеченный картофель'],3)
main()