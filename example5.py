class Summation:
    def sum(self, a, b):
        return a + b

    def __call__(self, a, b):
        return self.sum(a, b)


class Subtraction:
    def subtract(self, a, b):
        return a - b

    def __call__(self, a, b):
        self.subtract(a, b)


class Multiplication:
    def multiply(self, a, b):
        return a * b

    def __call__(self, a, b):
        self.multiply(a, b)


class Division:
    def divide(self, a, b):
        return a / b

    def __call__(self, a, b):
        self.divide(a, b)


class Calculator(Summation, Subtraction, Multiplication, Division):
    def __init__(self, operation):
        self.operation = operation

    def operate(self, x, y):
        if self.operation == 'add':
            return super().sum(x, y)
        elif self.operation == 'subtract':
            return super().subtract(x, y)
        elif self.operation == 'multiply':
            return super().multiply(x, y)
        elif self.operation == 'divide':
            return super().divide(x, y)
        else:
            print('Invalid operation')


if __name__ == '__main__':
    calc = Calculator("multiply").operate(5, 3)

    print(calc)

    s =Summation()(3,6)
    print(s)
    print(Calculator.__mro__)
