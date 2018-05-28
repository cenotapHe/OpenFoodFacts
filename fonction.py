# Importation of the different module
import mysql.connector
import sys

# Creation of printage fonction, for dodge the probleme of encodation coming to the sql file


def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    """ Just print fonction, without probleme of encodation from sql file."""
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        def f(obj): return str(obj).encode(
            enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)


def select_from(self):
    """With mySQL connector, this fonction do a SELECT FROM"""
    cnx = mysql.connector.connect(
        host='localhost', database='openfoodfacts', user='user', password='password')

    cursor = cnx.cursor()

    query = (self)
    cursor.execute(query)

    tupple = []

    for i in cursor:
        variable = i
        tupple.append(variable)

    return tupple


def update(self):
    """With mySQL connection, this fonction do another fonction from python to mySQL database"""
    cnx = mysql.connector.connect(
        host='localhost', database='openfoodfacts', user='user', password='password')

    cursor = cnx.cursor()

    query = (self)

    cursor.execute(query)

    cnx.commit()


def nutriscore(self):
    """This fonction convert the nutriscore number in a nutriscore letter"""
    if self == 1:
        variable = "nutriscore = A"
    elif self == 2:
        variable = "nutriscore = B"
    elif self == 3:
        variable = "nutriscore = C"
    elif self == 4:
        variable = "nutriscore = D"
    else:
        variable = "nutriscore = E"

    return variable
