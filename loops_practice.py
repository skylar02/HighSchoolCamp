"""
title: loops_practice
author: Skylar
date: 2019-06-13 13:38
"""
num = [89, 41, 73, 90]
for i in num:
    print(i)

print('\n')


for i in range(5, 15):
    print(i)

print('\n')

for i in range(100, 201, 10):
    print(i)

print('\n')

for i in range(80, 31, -8):
    print(i)

print('\n')

for i in range(3):
    print("Alright")

print('\n')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num = 0
for i in numbers:
    if(i % 2) == 1:
        num = num+2
        print(num)

print('\n')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num = 0
for i in numbers:
    if(i % 2) == 1:
        num = num+1
        print(num)

print('\n')

count = 11
while count > 1:
    count = count - 1
    print(count)

print('\n')


inp = input("Enter num > 0: ")

while inp != "0":
    inp = input("Enter num > 0: ")

print("Thank you")

print('\n')

f = int(input("Enter a small num"))
s = int(input("Enter a large num"))

print(f)
while f < s:
    f += 1
    print(f)

print('\n')


inf = input("Respond: ")

while inf != 'Y'or inf != 'y'or inf != 'yes'or inf != 'YES' or 'N'or inf != 'n'or inf != 'no'or inf != 'NO':
    inf = input("Respond: ")

print("Thx")
