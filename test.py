class Adder:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2


def main():
    # Get input from user
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    # Create object of Adder class
    calculator = Adder(number1, number2)

    # Call add method
    result = calculator.add()

    print("The sum is:", result)


if __name__ == "__main__":
    main()