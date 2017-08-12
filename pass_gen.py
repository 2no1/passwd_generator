import argparse
import random
from argparse import RawTextHelpFormatter
parser = argparse.ArgumentParser(description='Options are:\n1. Numbers only \n2. Lower letters only \n3.Upper letters only \n4. Lower letters and numbers \n5. Upper letters and numbers \n6. Upper and lower letters \n7. 100% random ', formatter_class=RawTextHelpFormatter)
parser.add_argument("count", help="number of choices", type=int)
parser.add_argument("length", help="length for passwd", type=int)
parser.add_argument("-op", "--option", type=int)
args = parser.parse_args()

c = (args.count)
l = (args.length)

if args.option == 1:
	for _ in range(c):
		qq = ''.join(random.choice("1234567890") for _ in range(l))
		print('')
		print(qq)
		print('')
elif args.option == 2:
    for _ in range(c):
        qq = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(l))
        print('')
        print(qq)
	print('')
elif args.option == 3:
    for _ in range(c):
        qq = ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(l))
        print('')
        print(qq)
	print('')
elif args.option == 4:
    for _ in range(c):
        qq = ''.join(random.choice("1234567890abcdefghijklmnopqrstuvwxyz") for _ in range(l))
        print('')
        print(qq)
	print('')
elif args.option == 5:
    for _ in range(c):
        qq = ''.join(random.choice("1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(l))
        print('')
        print(qq)
	print('')
elif args.option == 6:
    for _ in range(c):
        qq = ''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(l))
        print('')
        print(qq)
	print('')
elif args.option == 7:
    for _ in range(c):
        qq = ''.join(random.choice("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(l))
        print('')
        print(qq)
	print('')
else:
	print('WRONG!!')
