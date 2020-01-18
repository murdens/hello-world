
print("hello")
inp = input("Which colour - blue, orange, yellow, green, red, purple, pink, black?\n")
if inp in 'blue''purple''yellow''black':
    inp = input('Which number 1, 3, 5, 7 ?\n')
    if inp == '1':
        print('jump 10 times')
    elif inp == '3':
        print('spin around')
    elif inp == '5':
        print('be a frog')
    elif inp == '7':
        print('meow like a cat')
else:
    inp = input('Which number 2, 4, 6, 8?\n')
    if inp == '2':
        print('do 5 pressups')
    elif inp == '4':
        print('be a tree')
    elif inp == '6':
        print('kiss')
    elif inp == '8':
        print('do 3 situps')
    quit()
