from pprint import pprint
import os
import json
import time

debut = time.time()

i = 3029330003433

count = 0

while i <= 3029330003533:

    os.system("curl -X GET https://fr.openfoodfacts.org/api/v0/produit/{}.json --output fichier.json".format(str(i)))

    json_data = open('fichier.json')

    data = json.load(json_data)

    try:
        bibliotheque = data['product']

        product_name = bibliotheque['product_name']
        product_generic_name = bibliotheque['generic_name_fr']
        product_nutriscore = bibliotheque['nutrition_grade_fr']
        product_stores = bibliotheque['stores']

        fichier = open("test.txt", "a")
        fichier.write("Je vous présente le " + product_name + " de la famille des " + product_generic_name + "\n")
        fichier.write("Il a un nutriscore égal à : " + product_nutriscore + ", et on peut l'acheter à : " + product_stores + "\n\n")
        fichier.close()

        count += 1

    except KeyError:
        pass

    json_data.close()
    os.remove('fichier.json')

    i += 1

print(count)

print(time.time() - debut)