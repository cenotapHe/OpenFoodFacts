import os
import sys

os.system('cls')

print("q - Quitter")
print("Appuyer sur n'importe quelle autre touche pour continuer d'utiliser ce programme.")
swap_answer = input(">>> ")

if swap_answer == "q":
	os.system('cls')
	sys.exit(0)

else:
	os.system('cls')
	os.system("py -3.4 main.py")
	sys.exit(0)

