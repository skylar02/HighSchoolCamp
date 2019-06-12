"""
title: random_practice
author: Skylar
date: 2019-06-12 09:53
"""
import random
name = (input("Enter your name"))
salary = int(input("Enter your salary"))
raise_per = random.randint(0, 100)
per = raise_per/100
raise_amount = salary * per + salary
print(name + ' ' + 'your current salary is'+ ' ' + str(salary) + '' + '.' + ' ' + 'Your raise is' + ' ' + str(raise_per)+'%' + ' ' +'of'+ ' '+str(salary)+'.'+' '+name+' '+'your new salary is'+' '+str(raise_amount))
