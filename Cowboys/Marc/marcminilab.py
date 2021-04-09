class Robot:
    def setName(self,n):
        self.name=n
    def getName(self):
        return self.name

    def setColor(self,c):
        self.color=c
    def getColor(self):
        return self.color

    def setWeight(self,w):
        self.weight=w
    def getWeight(self):
        return self.weight

    @property
    def display(self):
        return('Name:', self.name, 'Color:', self.color, 'Weight:', self.weight)



R=Robot()
R.setName("Tom")
R.setColor("Red")
R.setWeight(55)

class Calculator:
    def __init__(self, num1, num2):
        self.number_1=num1
        self.number_2=num2

    def add(self):
        return self.number_1+self.number_2

    def sub(self):
        return self.number_1-self.number_2

    def mul(self):
        return self.number_1*self.number_2

    def div(self):
        return self.number_1/self.number_2

class Robot1:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight