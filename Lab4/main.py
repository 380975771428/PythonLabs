from datetime import datetime
from retiree import Retiree

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
myFile = open(dir_path + '/' + 'data.txt', encoding='utf-8')


retirees = []

for row in myFile:
    print(row)
    data = row.split(';')
    retiree = Retiree(data[0], data[1], data[2], datetime(year=int(data[3]), month=int(data[4]), day=int(data[5])), int(data[6]), data[7], int(data[8]), int(data[9]))
    retirees.append(retiree)

sumAge, countFemale = 0, 0

for retiree in retirees:
    if retiree.sex == 'female':
        sumAge += retiree.retirementAge
        countFemale += 1

middleAge = 0
if countFemale != 0:
    middleAge = sumAge / countFemale

print('\nCередній вік виходу на пенсію жінок: ', middleAge)
print('Гроші які отримав пенсіонер від держави за час перебування на пенсії: ', retirees[0].getAllMoneyFromState())