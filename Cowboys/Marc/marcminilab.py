class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)

    def give_weight(self):
        print(self.name + " has a weight of " + self.weight + " pounds.")

    def give_color(self):
        print(self.name + " is " + self.color)

r1 = Robot("Tom", "Blue", "50")
r2 = Robot("Michael", "Green", "45")

r1.introduce_self()
r2.introduce_self()

r1.give_weight()
r2.give_weight()

r1.give_color()
r2.give_color()

class Calc():
    @staticmethod
    def add(x,y):
        return (x+y)

    @staticmethod
    def sub(x,y):
        return (x-y)

    @staticmethod
    def mul(x,y):
        return (x*y)

    @staticmethod
    def div(x,y):
        if y == 0:
            return "You cannot divide by zero"
        else:
            return x/y



print(Calc.add(3,4))
print(Calc.sub(20,6))
print(Calc.mul(5,3))
print(Calc.div(6,2))
print(Calc.div(5,0))
print(Calc.div(0,5))
