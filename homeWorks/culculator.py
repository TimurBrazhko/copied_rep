class Calculator:

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'{self.number}'

    def __add__(self, other):
        return Calculator(self.number + other)

    def __sub__(self, other):
        return Calculator(self.number - other)

    def __mul__(self, other):
        return Calculator(self.number * other)

    def __truediv__(self, other):
        return Calculator(self.number / other)


c1 = Calculator(100)
c1 = c1 * 100
print(c1)



