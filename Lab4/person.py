from datetime import date

class Person:
    def __init__(self, lastName, firstName, surname, birthday):
        self.lastName = lastName
        self.firstName = firstName
        self.surname = surname
        self.birthday = birthday

    def getAge(self):
        today = date.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
    