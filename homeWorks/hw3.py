class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.balance}'

    def moneyX(self):
        p1 = int(input("How much money would you like to give?"))
        self.balance += p1
        return self.balance

    def _kill(self):
        self.balance = 0
        return self.balance

    def __jackpot(self):
        self.balance *= 10
        return self.balance

    def _copybalance(self, other):
        self.balance += other.balance


timur = Bank("Timur", 100)
beka = Bank("Beka", 100)


timur.moneyX()
timur._Bank__jackpot()
timur._kill()
print(timur)
print(beka)
