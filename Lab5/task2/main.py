import sqlite3, os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
FILENAME = DIR_PATH + '/' + 'bank_clients.db'

def getConnection():
    return sqlite3.connect(FILENAME)

def createTables():
    with getConnection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                _id                 INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name          TEXT,
                last_name           TEXT,
                address             TEXT,
                sex                 TEXT,
                phone_number        TEXT,
                credit              INTEGER,
                birthday            DATE
            )
        """)

def deleteTable():
    try:
        with getConnection() as conn:
            cursor = conn.cursor()
            cursor.execute('DROP TABLE clients')
    except Exception:
        print('Table clients not found')


def insertData():
    try:
        with getConnection() as conn:
            print('----Insert data----')

            _id = None
            first_name = input('first_name: ')
            last_name = input('last_name: ')
            address = input('address: ')
            sex = input('sex: ')
            phone_number = input('phone_number: ')
            credit = int(input('credit: '))
            birthday = input('birthday (y.m.d): ')


            cursor = conn.cursor()
            cursor.execute('INSERT INTO clients VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (
                _id, first_name, last_name, address, sex, phone_number, credit, birthday
            ))
    except Exception:
        print('Something went wrong')

def showAllData():
    try:
        with getConnection() as conn:
            cursor = conn.cursor()

            cursor.execute('SELECT * FROM clients')
            print(cursor.fetchall())
    except Exception:
        print('Something went wrong')


def showData():
    try:
        with getConnection() as conn:
            cursor = conn.cursor()

            cursor.execute('SELECT first_name, last_name, MAX(birthday) FROM clients')
            res = str(cursor.fetchone())
            print("The youngest creditor: ", res[1:-2])

            cursor.execute('SELECT SUM(credit) FROM clients')
            res = str(cursor.fetchone())
            print("Total sum of credit: ", res[1:-2])
    except Exception:
        print('Something went wrong')

deleteTable()
createTables()
insertData()
showAllData()
showData()
