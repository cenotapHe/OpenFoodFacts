# coding: utf-8

import os
import json
import time

debut = time.time()

i = 1
i_max = 20

count = 0
list_category = []

i_category = 0
name_category = ['hamburgers', 'viennoiseries', 'bonbons', 'mueslis', 'pizzas']

while i <= i_max:

    os.system("curl -X GET https://fr-en.openfoodfacts.org/category/{}/{}.json --output fichier.json".format(name_category[i_category], str(i)))
    try:
        json_data = open('fichier.json')

        data = json.load(json_data)

    except UnicodeDecodeError:

        try:
            json_data.close()
            os.remove('fichier.json')
        except FileNotFoundError:
            pass

    except FileNotFoundError:
        try:
            json_data.close()
            os.remove('fichier.json')
        except FileNotFoundError:
            pass

    try:
        exterieur = data['products']

        k = 0

        try:
            while k <= 19:

                bibliotheque = exterieur[k]

                product_name = bibliotheque['product_name_fr']
                product_generic_name = name_category[i_category]
                product_nutriscore = bibliotheque['nutrition_grade_fr']
                product_stores = bibliotheque['stores']
                product_link = bibliotheque['ingredients_text_fr']

                if product_stores != '' and product_name != '':

                    h = 0
                    while h < len(product_name):
                        if product_name[h] == "'" or product_name[h] == '"':
                            product_name = product_name[:h] + \
                                " " + product_name[h + 1:]
                        h += 1
                    h = 0
                    while h < len(product_stores):
                        if product_stores[h] == "'" or product_stores[h] == '"':
                            product_stores = product_stores[:h] + \
                                " " + product_stores[h + 1:]
                        h += 1
                    h = 0
                    while h < len(product_link):
                        if product_link[h] == "'" or product_link[h] == '"':
                            product_link = product_link[:h] + \
                                " " + product_link[h + 1:]
                        h += 1

                    fichier = open("test.sql", "a")

                    if product_generic_name not in list_category:

                        fichier.write("INSERT INTO category\nVALUES (NULL, '" +
                                      product_generic_name + "');\n\n")

                        list_category.append(product_generic_name)

                    j = 0
                    while j < len(list_category):

                        if product_generic_name == list_category[j]:
                            product_number_category = j + 1

                        j += 1

                    product_nutriscore_number = ''

                    if product_nutriscore == 'a':
                        product_nutriscore_number = '1'
                    elif product_nutriscore == 'b':
                        product_nutriscore_number = '2'
                    elif product_nutriscore == 'c':
                        product_nutriscore_number = '3'
                    elif product_nutriscore == 'd':
                        product_nutriscore_number = '4'
                    else:
                        product_nutriscore_number = '5'

                    fichier.write("INSERT INTO product\nVALUES (NULL, " +
                                  str(product_number_category) + ", '" +
                                  product_name + "', '" +
                                  product_link + "', '" +
                                  product_stores + "', " +
                                  product_nutriscore_number + ", False);\n\n")
                    count += 1

                k += 1

        except IndexError:
            pass

        try:
            fichier.close()
        except NameError:
            pass

    except KeyError:
        pass
    except NameError:
        pass

    json_data.close()

    try:
        os.remove('fichier.json')
    except FileNotFoundError:
        pass

    if i == i_max:
        i_category += 1
        i = 0

    if i_category >= len(name_category):
        break

    i += 1

print("Nombre de référence recencée(s) : " + str(count))

print(time.time() - debut)
