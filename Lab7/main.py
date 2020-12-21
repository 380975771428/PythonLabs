from tkinter import *

class Form:
    def __init__(self, parent):
        Label(parent, text='Введіть перше число', pady=10, width=30).pack()
        self.entry1 = Entry(parent,  width=25)
        self.entry1.pack()
        self.err1 = Label(parent, text='', fg='red')
        self.err1.pack()

        Label(parent, text='Введіть друге число', pady=10, width=30).pack()
        self.entry2 = Entry(parent,  width=25)
        self.entry2.pack()
        self.err2 = Label(parent, text='', fg='red')
        self.err2.pack()

        Label(parent, text='Введіть третє число', pady=10, width=30).pack()
        self.entry3 = Entry(parent,  width=25)
        self.entry3.pack()
        self.err3 = Label(parent, text='', fg='red')
        self.err3.pack()

        self.multiply = BooleanVar()
        Radiobutton(parent, text='Різниця найбільшого і найменшого', pady=10, variable=self.multiply, value=0).pack()
        Radiobutton(parent, text='Сума найбільшого і найменшого', pady=10, variable=self.multiply, value=1).pack()

        self.submitBtn = Button(parent, text='Порахувати', command=self.submit, width=20)
        self.submitBtn.pack()

        self.resultLabel = Label(parent, text='', pady=10)
        self.resultLabel.pack()

    def submit(self):
        value1 = self.entry1.get()
        value2 = self.entry2.get()
        value3 = self.entry3.get()
        isMultiply = self.multiply.get()

        self.resultLabel['text'] = ''
        self.err1['text'] = ''
        self.err2['text'] = ''
        self.err3['text'] = ''
        self.err1['text'] = self.checkNumeric(value1)
        self.err1['text'] = self.checkEmpty(value1)
        self.err2['text'] = self.checkNumeric(value2)
        self.err2['text'] = self.checkEmpty(value2)
        self.err3['text'] = self.checkNumeric(value3)
        self.err3['text'] = self.checkEmpty(value3)

        if self.err1['text'] or self.err2['text'] or self.err3['text']:
            return


        num1 = int(value1)
        num2 = int(value2)
        num3 = int(value3)
        numMax = max(num1, num2, num3)
        numMin = min(num1, num2, num3)

        if isMultiply:
            self.result(numMax, numMin)
        else:
            self.result(numMax, -numMin)


    def checkNumeric(self, value):
        if not value.isnumeric():
            return 'Полe має містити лише числа'
        
    def checkEmpty(self, value):
        if not value:
            return 'Поле є обов\'язковим'

    def result(self, value1, value2):

        result = value1 + value2
        self.resultLabel['text'] = f'Результат: {result}'
        self.resultLabel['fg'] = 'black'
        return

root = Tk()
root.title('Варіант 10')
root.resizable(False, False)

x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))

Form(root)

root.mainloop()