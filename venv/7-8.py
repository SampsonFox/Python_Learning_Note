active = True
sandwiches_orders = {}
while active:
    name = input('What is your name：')
    order = input('What is your order: ')
    sandwiches_orders[name] = order
    other = input('Is there anyone else want to order? Y/N ')
    if other.upper() == 'Y':
        continue
    break

sandwiches_finished = {}

for key, value in sandwiches_orders.items():
    if value == 'pstrami':
        print('Sorry ' + key + ' but we dont have any pstrami left today!\n')
        continue
    print('The ' + value + ' is finished!\n')
    sandwiches_finished[key] = value

print(sandwiches_orders)
print(sandwiches_finished)

#遍历字典时不能改变字典元素

print('\nNo orders by now!\n')

for name, value in sandwiches_finished.items():
    print('Hi! ' + name + ', the order: ' + value + ' sandwich was complete!\n')
print('\n--------End of the list!---------')