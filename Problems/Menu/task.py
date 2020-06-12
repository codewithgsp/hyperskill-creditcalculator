option = input()
menu = {'pizza': 'Margarita, Four Seasons, Neapoletana, Vegetarian, Spicy',
        'salad': 'Caesar salad, Green salad, Tuna salad, Fruit salad',
        'soup': 'Chicken soup, Ramen, Tomato soup, Mushroom cream soup'}
if option in menu.keys():
    print(menu[option])
else:
    print("Sorry, we don't have it in the menu")
