import mysql.connector
import sys


def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        def f(obj): return str(obj).encode(
            enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)


def select_from(self):

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

    cnx = mysql.connector.connect(
        host='localhost', database='openfoodfacts', user='edward', password='josephsnowden')

    cursor = cnx.cursor()

    query = (self)

    cursor.execute(query)

    cnx.commit()


def nutriscore(self):

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
