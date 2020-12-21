from person import Person

class Retiree(Person):
    def __init__(self, lastName, firstName, surname, birthday, retirementAge, sex, amountPension, experience):
        Person.__init__(self, lastName, firstName, surname, birthday)

        self.retirementAge = retirementAge
        self.sex = sex
        self.amountPension = amountPension
        self.experience = experience


    def getAllMoneyFromState(self):
        ageOfRetiree = self.getAge() - self.retirementAge
        return ageOfRetiree * self.amountPension