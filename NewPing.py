import os
import sys

def menu():
    print('*'*7,'Menu','*'*7)
    print('* 1. List of URL   *')
    print('* 2. Enter URL     *')
    print('* 3. Exit          *')
    print('*'*20)
    choice = int(input('Enter Choice: '))
    pick(choice)


def pick(choice):
    if choice == 1:
        print('*'*9,'List','*'*9,
        '\n* 1:Google             *',
        '\n* 2.Amazon      *',
        '\n* 3.Youtube  *',
        '\n* 0.Head back to Menu  *')
        print('*'*24)
        choice2 = int(input('Enter Choice: '))
        if choice2 == 0:
            menu()
        elif choice2 == 1:
            os.system("ping %s" %('google.com'))
        elif choice2 == 2:
            os.system("ping %s" %('amazon.com'))
        elif choice2 == 3:
            os.system("ping %s" %('youtube.com'))
    elif choice == 2:
        url = input('Enter URL: ')
        os.system("ping %s" %url)
    elif choice == 3:
        sys.exit()
    else:
        print('Error pick from the following Menu\n')
        menu()

menu()
