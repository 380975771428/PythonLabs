import ZODB, ZODB.FileStorage, transaction
from bankCustomer import BankCustomer

storage = ZODB.FileStorage.FileStorage('bank')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()


lastName = input('lastName: ')
firstName = input('firstName: ')
address  = input('address: ')
sex = input('sex: ')
sumCredit = int(input('sumCredit: '))
birthday = input('birthday (y.m.d): ').split('.')

bankCustomers = root['bank']
bankCustomers.append(BankCustomer(lastName, firstName, address, birthday, sex, sumCredit))
root['bank'] = bankCustomers

transaction.commit()