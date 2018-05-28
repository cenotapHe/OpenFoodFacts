# coding: utf-8

# Importation of the different module
import sys
import os
import random
import mysql.connector
from fonction import *

# Start menu of the application
os.system('cls')
print("1 - Trouver un aliment que vous souhaitez remplacer.")
print("2 - Retrouver mes aliments précedements substitués.")
print("q - Quitter.")
choice = ["1", "2", "q"]
answer = input(">>> ")

# Catch the wrong answer
while answer not in choice:
    print("Ce choix n'est pas valide.")
    answer = input(">>> ")

if answer == "q":
    sys.exit(0)

# Menu for choice the category of food
if answer == "1":
    os.system('cls')
    print("Choissisez votre catégorie :")

    # Using fonction of fonction.py for request SELECT FROM in your database
    query = "SELECT category_id, name FROM category"
    category_tupple = select_from(query)

    category_choice = ["q"]
    for i in enumerate(category_tupple):
        print(i[1])
        category_choice.append(str(i[1][0]))

    print("q - Quitter")

    category_answer = input(">>> ")

    # Catch the wrong answer
    while category_answer not in category_choice:
        print("Ce choix n'est pas valide.")
        category_answer = input(">>> ")

    if category_answer == "q":
        sys.exit(0)

    # Menu for choice the product in the category choosen
    os.system('cls')
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

    # Catche the wrong answer
    while product_answer not in product_choice:
        print("Ce choix n'est pas valide.")
        product_answer = input(">>> ")

    if product_answer == "q":
        sys.exit(0)

    # Using fonction of fonction.py for request SELECT FROM in your database
    query = "SELECT name, description, nutriscore, store FROM product WHERE id = " + \
        str(product_answer)
    product_final = select_from(query)

    # Display the product properly
    os.system('cls')
    uprint(" ", product_final[0][0], "\n@ " +
           product_final[0][3] + "\n\nIngrédients:")
    if product_final[0][1] == "":
        print(" Nous n'avons pas la liste des ingrédients pour ce produit, désolé.")
    else:
        uprint(" " + product_final[0][1] + "\n")
    print(" " + nutriscore(product_final[0][2]) + "\n")
    input(">>> ")

    final_boucle = True
    # The file seeking another product in the category and compare the nutriscore
    while final_boucle:
        query = "SELECT nutriscore FROM product WHERE id = " + \
            str(product_answer)
        product_final = select_from(query)

        if str(product_final[0][0]) == "1":
            print(
                "Ce produit a déjà un nutriscore égal à A. Il n'y pas pas besoin de le substituer")

        else:
            try:
                # Display the substitu properly
                query = "SELECT id, name, nutriscore, store, description FROM product WHERE category_id = " + \
                    str(category_answer) + " AND nutriscore < " + \
                    str(product_final[0][0])
                substitut_tupple = select_from(query)
                i = random.randint(0, len(substitut_tupple) - 1)
                substitut = substitut_tupple[i]
                uprint("\n", substitut[1], "\n@", substitut[3], "\n\nIngrédients:\n",
                       substitut[4], "\n\n", nutriscore(substitut[2]), "\n")

            except ValueError:
                # The product is the best in his category
                print(
                    "\nMalheureusement (ou bienheureusement selon le point de vue), il n'existe aucun produit de qualité supérieur dans cette catégorie.")
                input("\nAppuyer sur 'Enter' pour continuer.")
                os.system('cls')
                os.system("py swap.py")
                sys.exit(0)
        replace_choice = ["1", "2", "q"]
        # Chose after the substitut
        print("1 - Sauvegarde du substitut pour cet article.")
        print("2 - Chercher un nouveau substitut pour cet article.")
        print("q - Retour.")
        replace_answer = input(">>> ")

        while replace_answer not in replace_choice:
            print("Ce choix n'est pas valide.")
            replace_answer = input(">>> ")

        # Use swap.py for choice if you want to continue or quit
        if replace_answer == "q":
            os.system('cls')
            os.system("py swap.py")
            sys.exit(0)

        # Save the product and the substitut in the database
        if replace_answer == "1":
            final_boucle = False
            query = "UPDATE product SET register = True WHERE id = " + \
                str(product_answer)
            update(query)
            query = "UPDATE product SET substitut_id = " + \
                str(substitut[0]) + " WHERE id = " + str(product_answer)
            update(query)
            os.system('cls')
            print("Le produit a bien été substitué.")
            os.system("py swap.py")
            sys.exit(0)

        # If only one substitut exist, the system signal this
        if replace_answer == "2":
            if len(substitut_tupple) == 1:
                print(
                    "\nDésolé, mais il n'existe pas d'autre substitut valide dans cette catégorie.\n")

# When the user want to see the database of the subsitued product
if answer == "2":

    os.system('cls')

    query = "SELECT id, name, store, substitut_id, nutriscore FROM product WHERE register = True"

    category_tupple = select_from(query)

    # Display properly the substitued product
    try:
        for i in enumerate(category_tupple):
            query = "SELECT id, name, store, nutriscore FROM product WHERE id = " + \
                str(i[1][3])
            substitut_comparaison = select_from(query)
            uprint("\n" + str(i[1][1]) + " @ " + str(i[1][2]) + " substitué par " +
                   str(substitut_comparaison[0][1]) + " @ " + str(substitut_comparaison[0][2]))
            print(nutriscore(i[1][4]) + " VersuS " +
                  nutriscore(substitut_comparaison[0][3]))
    except:
        pass

    # Utilisation for reset the database of the substitued product
    print("\nTapez 'RAZ' pour une remise à zéro de tous les ingrédients substitués. (AUCUN RETOUR EN ARRIERE POSSIBLE)\nAppuyez sur n'importe qu'elle autre touche pour continuer.")
    RAZ = input(">>> ")
    if RAZ == "RAZ":
        query = "UPDATE product SET substitut_id = NULL WHERE register = True"
        update(query)
        query = "UPDATE product SET register = False WHERE register = True"
        update(query)
        input("La base de données a bien été remise à Zéro.")

    os.system('cls')
    os.system("py swap.py")
    sys.exit(0)
