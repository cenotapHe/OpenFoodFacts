# Importation of different module
import os
import sys

os.system('cls')

# Made a choice for the user of the application
print("q - Quitter")
print("Appuyer sur n'importe quelle autre touche pour continuer d'utiliser ce programme.")
swap_answer = input(">>> ")

# If the user want to quit, the application quit
if swap_answer == "q":
    os.system('cls')
    sys.exit(0)

# If the user want to use again, this file launch main.py
else:
    os.system('cls')
    os.system("py -3.4 main.py")
    sys.exit(0)
