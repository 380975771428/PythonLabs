class BankCustomer:
    def __init__(self, lastName, firstName, address, birthday, sex, sumCredit):
        self.lastName = lastName
        self.firstName = firstName
        self.address = address
        self.birthday = birthday
        self.sex = sex
        self.sumCredit = sumCredit

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}' \
            .format(self.lastName, self.firstName, self.address, self.birthday, self.sex, self.sumCredit)