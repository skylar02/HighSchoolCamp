"""
title: string_practice
author: Skylar
date: 2019-06-11 13:45
"""
import random
chara = input("Enter a character")
print("a" in chara or "b" in chara or "c" in chara or "d" in chara or "e" in chara or "f" in chara or "g" in chara or "h" in chara or "i" in chara or "j" in chara or "k" in chara or "l" in chara or "m" in chara or "n" in chara or "o" in chara or "p" in chara or "q" in chara or "r" in chara or "s" in chara or "t" in chara or "u" in chara or "v" in chara or "w" in chara or "x" in chara or "y" in chara or "z" in chara)


short = input("Enter a greeting here")
short_hand = short.replace("and", "&").replace("too", "2").replace("you", "U").replace("for", "4").replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")
print(short_hand)

fn = input("Enter your first name")
ln = input("Enter your last name")
cn = input("Enter birth city")
ug = input("Enter Alma Mater university")
rn = input("Enter a relative's name")
frn = input("Enter a friend's name")

print(fn[:4] + ln[-3:]) + cn[:3] + ug[-4:] + rn[random.randint(0,len(rn)):-1] + fn[0:random.randint(len(frn))]































