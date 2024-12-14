class Calculator:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)
    def add(self):
        return self.a + self.b
    def subtract(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Division by zero is not allowed"
    def calculate(self, operation):
        if operation == 'add':
            return self.add()
        elif operation == 'subtract':
            return self.subtract()
        elif operation == 'multiply':
            return self.multiply()
        elif operation == 'divide':
            return self.divide()
        else:
            return "Invalid operation"
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
operation = input("Enter the type of operation (add, subtract, multiply, divide): ").strip().lower()
calculator = Calculator(a, b)
result = calculator.calculate(operation)
print("Result:", result)
