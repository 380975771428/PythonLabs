import re
a = re.split('[.,!?/<>1234567890 ]+', input())
print(a)

for word in a:
    if a.count(word) == 1:
        print(word, end=" ")




