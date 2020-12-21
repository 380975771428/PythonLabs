def changeSum(dataDict, key, money):
    if key in dataDict:
        dataDict[key] += money
    else:
        dataDict[key] = money

num = int(input("Enter count of operations: "))
dataDict = dict()
res = ''

for i in range(num):
    op = input().split()
    if op[0] == 'DEPOSIT':
        changeSum(dataDict, op[1], int(op[2]))

    elif op[0] == 'WITHDRAW': 
        changeSum(dataDict, op[1], -int(op[2]))
    
    elif op[0] == 'TRANSFER':
        changeSum(dataDict, op[1], -int(op[3]))
        changeSum(dataDict, op[2], int(op[3]))

    elif op[0] == 'INCOME':
        for key in dataDict:
            if dataDict[key] >= 0:
                dataDict[key] += int(op[1])

    elif op[0] == 'BALANCE':
        if op[1] in dataDict:
            res += str(dataDict[op[1]]) + '\n'
        else:
            res += 'ERROR' + '\n'

print(res)