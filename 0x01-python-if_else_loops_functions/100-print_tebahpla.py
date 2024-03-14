#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        gap = 0
    else:
        gap = 32
    print('{}'.format(chr(i - gap)), end='')
