# coding: utf-8

import sqlite3
import os

connection = sqlite3.connect("OpenFoodFacts.db")

cursor = connection.cursor()


my_file = open("Database_MySQL_for_script.sql", "r")
all_my_file = my_file.read()

count = 0

for i in enumerate(all_my_file):
    if i[1] == ";":

        sql_command = all_my_file[count:i[0] + 1]

        count = i[0] + 1

        print(sql_command)

        cursor.execute(sql_command)

my_file.close()

my_file = open("test.sql", "r")
all_my_file = my_file.read()

print(type(all_my_file))
count = 0

for i in enumerate(all_my_file):
    if i[1] == ";":

        sql_command = all_my_file[count:i[0] + 1]
        print(sql_command)

        count = i[0] + 1

        cursor.execute(sql_command)

my_file.close()

connection.close()
