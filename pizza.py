def making_pizza(size, *toppings):
    """描述披萨"""
    print('\nU have ordered a ' + str(size) + ' size pizza with ')
    for topping in toppings:
        print(topping)
    print('as topping/s!')