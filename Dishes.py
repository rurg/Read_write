from pprint import pprint

def receipt_read(receipt):
    Ing = []
    CookBook = {}

    with open(receipt) as r:
        while True:
            dish_list = []
            dish_name = r.readline().rstrip()
            #        print(dish_name)
            NumIngredients = r.readline().rstrip()
            #        print(NumIngredients)
            if not dish_name and not NumIngredients:
                break
            #   Здесь поднимается ошибка Value Error если использовать генератор списков,
            #   и разобраться с этим не получилось
            #        Ing = [r.readline().rstrip() for Ingredient in range(int(NumIngredients))]
            #        print(Ing)
            try:
                for Ingredient in range(int(NumIngredients)):
                    Ingredient = r.readline().rstrip()
                    #                print(Ingredient)
                    Ing = Ingredient.split(' | ')
                    Ing_dict = {"Ingredient":Ing[0],"quantity":int(Ing[1]),"мeasure":Ing[2]}
                    dish_list.append(Ing_dict)
            except ValueError:
                print('Ошибка была')
            #        pprint(dish_list)
            CookBook.update({dish_name:dish_list})
            r.readline()
        return CookBook
CookBook = receipt_read('receipt.txt')

pprint(CookBook)

person = 3
i = 0
ingridients_for_dish = {}
ToCook = ['Каша из Топора','Омлет','Попеченный картофель']
Number_person = int(2)

try:
    for DishToCook in ToCook:
        #        pprint (CookBook[DishToCook])
        for ing in CookBook[DishToCook]:
            new_ingridient_for_dish = ing
            new_ingridient_for_dish['quantity'] *= person
            print(new_ingridient_for_dish)
            if new_ingridient_for_dish['Ingredient'] not in ingridients_for_dish:
                ingridients_for_dish[new_ingridient_for_dish['Ingredient']] = new_ingridient_for_dish
            else:
                ingridients_for_dish[new_ingridient_for_dish['Ingredient']]['quantity'] += new_ingridient_for_dish['quantity']
#            print(new_ingridient_for_dish)
#                pprint(ingridients_for_dish)




except KeyError:
    print('отсутсвующее или неверно-введенное блюдо')
    pass
