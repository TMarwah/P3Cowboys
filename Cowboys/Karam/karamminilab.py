class Caracal:

    # Class Variable
    animal = 'caracal'

    # The init method or constructor
    def __init__(self, weight, color):

        # Instance Variable
        self.weight = weight
        self.color = color

    # Objects of Caracal class
Zabloing = Caracal("skinny", "beige")
Floppa = Caracal("fat", "brown")

print('Zabloing details:')
print('Zabloing is a', Zabloing.animal)
print('weight: ', Zabloing.weight)
print('color: ', Zabloing.color)

print('\nFloppa details:')
print('Floppa is a', Floppa.animal)
print('weight: ', Floppa.weight)
print('color: ', Floppa.color)

# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Caracal.animal)

class Calculator:
    def __init__(self, x, y):
        self.x= x
        self.y= y

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def mul(self):
        return self.x * self.y

    def div(self):
        return self.x / self.y

