"""
title: string_practice
author: Skylar
date: 2019-06-11 13:45
"""
import random
#chara = input("Enter a character")
#print("a" in chara or "b" in chara or "c" in chara or "d" in chara or "e" in chara or "f" in chara or "g" in chara or "h" in chara or "i" in chara or "j" in chara or "k" in chara or "l" in chara or "m" in chara or "n" in chara or "o" in chara or "p" in chara or "q" in chara or "r" in chara or "s" in chara or "t" in chara or "u" in chara or "v" in chara or "w" in chara or "x" in chara or "y" in chara or "z" in chara)


#short = input("Enter a greeting here")
#short_hand = short.replace("and", "&").replace("too", "2").replace("you", "U").replace("for", "4").replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")
#print(short_hand)

#fn = input("Enter your first name")
#ln = input("Enter your last name")
#cn = input("Enter birth city")
#ug = input("Enter Alma Mater university")
#rn = input("Enter a relative's name")
#frn = input("Enter a friend's name")

#print(fn[:4] + str(ln[-3:])) + cn[:3] + ug[-4:] + rn[str(random.randint(0,len(rn))):-1] + fn[0:str(random.randint(len(frn)))]

#phrase = "Don't count your chickens before the hatch"
#slogan = "For everything else, there's mastercard"
#combined = f"{phrase}. {slogan}"

#print(combined)
#print(phrase[::2])
#print(phrase[17:25])
#print('m' in slogan)
#print(combined.upper())
#print(''.join(combined))
#print(slogan[::-1])


def is_letter(chara):
    return chara.lower() in "qwertyuiopasdfghjklzxcvbnm"


print(is_letter("qwertyuiop"))
print(is_letter('0'))


def short_hand(short):
    short = short.replace("and", "&").replace("too", "2").replace("you", "U").replace("for", "4")
    short = short.replace("a","").replace("e", "").replace("i", "").replace("o", "").replace("u", "")
    return short



inp = input("Enter a phrase:")
print(short_hand(inp))


def cred(fn, ln, cb, u, rn, fr):
    fn = fn[:3]
    ln = ln[-2:]
    cb = cb[:2]
    u = u[-3:]
    rn = rn[random.randint(0,len(rn)):]
    fr = fr[:random.randint(0,len(fr))]
    return fn+ln+cb+u+rn+fr


f = input("Enter your first name")
s = input("Enter your last name")
t = input("Enter the city you were born in")
fo = input("Enter the university you graduated from")
fi = input("Enter the name of a relative")
si = input("Enter the name of a friend")
print(cred(f, s, t, fo, fi, si))


def removing(check):
    check = check.lower()
    check = check.replace(" ", "").replace(",", "").replace("'", "")
    return check


er = input("Enter stuff")
print(removing(er))


def palindrome(check):
    check = removing(check)
    return check in check[::-1]


oyu = input("Enter more stuff")
print(palindrome(oyu))










