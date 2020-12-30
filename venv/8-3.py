def make_shirt(shirt_size='Large', shirt_style='I love Python'):
    print('\nThe shirt size is ' + shirt_size +'\nthe words is "' + shirt_style + '"\n')
    shirt_info = {'size':shirt_size, 'words':shirt_style}
    return shirt_info
active = True
while active:
    size = input('\nPlz selet shirt size: ')
    if size == 'q':
        break
    word = input('Plz say something: ')
    if word == 'q':
        break
    if size and not word:
        shirt_info = make_shirt(shirt_size=size)
    elif not size and word:
        shirt_info = make_shirt(shirt_style=word)
    elif size and word:
        shirt_info = make_shirt(shirt_size=size, shirt_style=word)
    else:
        shirt_info = make_shirt()
    print(shirt_info)
print('\n-----------END of the program-------------')