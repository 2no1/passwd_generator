import random

def numsonly():
    c = int(input('number of choices: '))
    l = int(input('length of string: '))
    for _ in range(c):
        qq = ''.join(random.choice("1234567890") for _ in range(l))
        print('')
        print(qq)
def letterlow():
    c = int(input('number of choices: '))
    l = int(input('length of string: '))
    for _ in range(c):
        qq = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(l))
        print('')
        print(qq)
def letterup():
    c = int(input('number of choices: '))
    l = int(input('length of string: '))
    for _ in range(c):
        qq = ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(l))
        print('')
        print(qq)
def lnlow():
    c = int(input('number of choices: '))
    l = int(input('length of string: '))
    for _ in range(c):
        qq = ''.join(random.choice("1234567890abcdefghijklmnopqrstuvwxyz") for _ in range(l))
        print('')
        print(qq)
def lnup():
    c = int(input('number of choices: '))
    l = int(input('length of string: '))
    for _ in range(c):
        qq = ''.join(random.choice("1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(l))
        print('')
        print(qq)
def lettersonly():
    c = int(input('number of choices: '))
    l = int(input('length of string: '))
    for _ in range(c):
        qq = ''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(l))
        print('')
        print(qq)
def super():   
    c = int(input('number of choices: '))
    l = int(input('length of string: '))
    for _ in range(c):
        qq = ''.join(random.choice("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(l))
        print('')
        print(qq)
       
def menu():
    print('1. numbers only')
    print('2. letters only (lower case)')
    print('3. letters only (upper case)')
    print('4. letters(lower case) and numbers')
    print('5. letters(upper case) and numbers')
    print('6. letters(lower and upper case)')
    print('7. 100% random')
    op = input('Please choose: ')
    if op == '1':
        numsonly()
    elif op == '2':
        letterlow()
    elif op == '3':
        letterup()
    elif op == '4':
        lnlow()
    elif op == '5':
        lnup()
    elif op == '6':
        lettersonly()
    elif op == '7':
        super()
    else:
        print('WRONG!!')
       
menu()
