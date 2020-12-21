# -*- coding: cp1251 -*-

import cgi

form = cgi.FieldStorage()

num1 = form.getfirst('firstNum')
num2 = form.getfirst('secondNum')
num3 = form.getfirst('thirdNum')
res = ''

if num1 is None or num2 is None or num3 is None:
    res = "Ви передали пусте поле"
else:
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)

    max_num = max(num1, num2, num3)
    min_num = min(num1, num2, num3)

    res = 'Результат: ' + str(max_num - min_num)


print('Content-type: text/html\n')
print("""<!DOCTYPE HTML>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
            <title>Лабораторна №6</title>
        </head>
        <body>""")

print(f'<h1  align="center">{res}</h1>')
print("""
    <form action="../" align="center">
    <input type="submit" value="Назад" class="btn btn-primary">
    </form>
""")

print('</body></html>')

