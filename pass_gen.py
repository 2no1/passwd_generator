import random
c = int(input('number of choices: '))
l = int(input('lenght of string: '))
for _ in range(c):
	qq = ''.join(random.choice("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(l))
	print(qq)
