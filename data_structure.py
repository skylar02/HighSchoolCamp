"""
title: data_structure
author: Skylar
date: 2019-06-13 11:31
"""
import random


def shake_ball():
    ret = input("Ask a question")
    ans = ("Yes definitely", "As I see it, yes", "Ask again later", "Cannot predict now", "Don't count on it", "Very doubtful")
    return ans[random.randint(0, len(ans))]


print(shake_ball())


def gymnast_scores():
    num = ("1", "2", "3", "4", "5")
    return num[random.randint(0, len(num)-1)]


num = ("1", "2", "3", "4", "5")
print("The lowest possible score is", str(num[0]), ", and the highest possible score is", str(num[4]), ".")
print("A judge can give a gymnast", (gymnast_scores()), "points.")


def remove_duplicates(mess):
    ans = 0