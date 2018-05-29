# OpenFoodFacts

An application for the fifth Project of DA Python

OpenFoodFacts is a application coding in Python.

## Befor using the application

### Desciption of all item

* Livrable
```
 - Link for the Trello
 - Image of the "Modèle Physique de Données"
 - Presentation of this application in a powerpoint
 - Text file of the application's development
```

* Script
```
 - script_python_for_db_file : create a .db with the data from OpenFoodFacts
 - script_python_for_sql_file : create a .sql with the data from OpenFoodFacts
 - Database_MySQL.sql : create table on your MySQL database
 - Database_MySQL.sql_for_script_python_for_db_file : using by script_python_for_db_file
 ```

* Python's files

## Description of the user's route

The user is on the terminal. The terminal display two choice :

1 - Which food do you want to replace ?

2 - Find my substitued foods.

When the user select 1. The application awser these questions to the user and the user select these responses :

* Select the category. [Further proposals are associated to a number. The user enter the corresponding number and press "Enter".]
* Select food. [PlusieursFurther proposals are associated to a number. The user enter the corresponding number and press "Enter".]
* The application propose a substitute, its description, a store to buy it and a link to the page Open Food Facts of this food.
* The user can saved the result in the database.

## Functionality

1 - Search of food in the database Open Food Facts.

2 - The user use the application in the terminal.

3 - If the user enter a character that is not a number, the application repeat the question again.

4 - The research occurs on a MySQL base.

## Getting Started

For launch the application use "main.py".

### Prerequisites

Your need to have Python v3.x install on your machine.

* [Python](https://www.python.org/downloads/) - The link for download Python from the website.
* [MySQL]() - 
* [MySQL Connector]() -

### Installing

This application doesn't need installation for works. Just launch "main.py" with python.

Example with the console, in the file download :

For Windows

```
py main.py
```

For Linux

```
python3 main.py
```

## Deployment

This game is developped  as part of the project "Utilisez les données publiques de l'OpenFoodFacts", belonging to the course "Développeur-se d'application - Python" from the platforme OpenClassrooms.

## Built With

* [MySQL](https://www.mysql.com/) - MySQL (officially pronounced as /maɪ ˌɛskjuːˈɛl/ "My S-Q-L",[5]) is an open-source relational database management system (RDBMS)..

## Contributing

PRIEUR Benoît - Mentor for this project

## Versioning

We use only [GitHub](https://github.com/cenotapHe/OpenFoodFacts) for versioning.

## Authors

* **Baptiste "cenotapHe" Carrasco** - *Initial work* - [cenotapHe](https://github.com/cenotapHe)

## License

This project is entire Open-Source.

## Acknowledgments

* OpenClassrooms, to give me the chance to train myself
* Python, to be so cool and so fun
