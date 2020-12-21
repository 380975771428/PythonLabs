import ZODB, ZODB.FileStorage, BTrees.OOBTree, transaction
from bankCustomer import BankCustomer


storage = ZODB.FileStorage.FileStorage('bank')
db = ZODB.DB (storage)
connection = db.open()
root = connection.root()

banks = list(filter(lambda s: s.bank.lower() == bank.lower(), root['bank']))

if len(banks) == 0 :
    print("No banks with such customer")
    exit()

oldest_bank = min(banks, key=lambda s: int(s.built_year))
bank_capacity = sum(int(bank.capacity) for bank in banks)

print("The oldest bank: ", oldest_bank)
print("Summary capacity: ", bank_capacity)