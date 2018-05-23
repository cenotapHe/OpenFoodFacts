# coding: utf-8

import sys
import os
import random
import mysql.connector
from fonction import *


print("1 - Quel aliment souhaitez-vous remplacer ?")
print("2 - Retrouver mes aliments substitués.")
print("q - Quitter.")
choice = ["1", "2", "q"]
answer = input(">>> ")

while answer not in choice:
    print("Ce choix n'est pas valide.")
    answer = input(">>> ")

if answer == "q":
    sys.exit(0)

if answer == "1":
    print("Choissisez votre catégorie :")

    query = "SELECT category_id, name FROM category"
    category_tupple = select_from(query)

    category_choice = ["q"]
    for i in enumerate(category_tupple):
        print(i[1])
        category_choice.append(str(i[1][0]))

    print("q - Quitter")

    category_answer = input(">>> ")

    while category_answer not in category_choice:
        print("Ce choix n'est pas valide.")
        category_answer = input(">>> ")

    if category_answer == "q":
        sys.exit(0)

    print("Choissisez votre produit :")

    query = "SELECT id, name FROM product WHERE category_id = " + \
        str(category_answer)
    product_tupple = select_from(query)

    product_choice = ["q"]
    for i in enumerate(product_tupple):
        uprint(i[1])
        product_choice.append(str(i[1][0]))

    print("q - Quitter")

    product_answer = input(">>> ")

    while product_answer not in product_choice:
        print("Ce choix n'est pas valide.")
        product_answer = input(">>> ")

    if product_answer == "q":
        sys.exit(0)

    query = "SELECT name, description FROM product WHERE id = " + \
        str(product_answer)
    product_final = select_from(query)

    uprint(product_final[0][0])
    uprint(product_final[0][1])
    print("Voulez-vous substituer ce produit ? (y/n)")
    substitut_answer = input(">>> ")

    if substitut_answer == "n":
        sys.exit(0)

    substitut_choice = ["y", "n"]

    while substitut_answer not in substitut_choice:
        print("Ce choix n'est pas valide.")
        substitut_answer = input(">>> ")

    query = "SELECT nutriscore FROM product WHERE id = " + str(product_answer)
    product_final = select_from(query)

    final_boucle = True

    while final_boucle:

        if str(product_final[0][0]) == "1":
            print(
                "Ce produit a déjà un nutriscore égal à A. Il n'y pas pas besoin de le substituer")

        else:
            try:
                query = "SELECT id, name, nutriscore, store FROM product WHERE category_id = " + \
                    str(category_answer) + " AND nutriscore < " + \
                    str(product_final[0][0])
                substitut_tupple = select_from(query)
                i = random.randint(0, len(substitut_tupple) - 1)
                substitut = substitut_tupple[i]
                uprint(substitut)

            except ValueError:
                print(
                    "Malheureusement, il n'existe aucun produit de qualité supérieur dans cette catégorie.")
                sys.exit(0)
        replace_choice = ["1", "2", "q"]
        print("1 - Sauvegarde du substitut pour cet article.")
        print("2 - Chercher un nouveau substitut pour cet article.")
        print("q - Quitter.")
        replace_answer = input(">>> ")

        while replace_answer not in replace_choice:
            print("Ce choix n'est pas valide.")
            substitut_answer = input(">>> ")

        if replace_answer == "q":
            sys.exit(0)

        if replace_answer == "1":
            final_boucle = False

        if replace_answer == "2":
            continue


if answer == "2":

    query = "SELECT id, name, nutriscore, name FROM product WHERE register = True"

    category_tupple = select_from(query)
