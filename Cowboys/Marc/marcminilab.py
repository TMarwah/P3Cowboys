
# class Calc():
#     @staticmethod
#     def add(x,y):
#         return (x+y)
#
#     @staticmethod
#     def sub(x,y):
#         return (x-y)
#
#     @staticmethod
#     def mul(x,y):
#         return (x*y)
#
#     @staticmethod
#     def div(x,y):
#         if y == 0:
#             return "You cannot divide by zero"
#         else:
#             return x/y
#
#
#
# print(Calc.add(3,4))
# print(Calc.sub(20,6))
# print(Calc.mul(5,3))
# print(Calc.div(6,2))
# print(Calc.div(5,0))
# print(Calc.div(0,5))

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

    def display(self):
        print('Name:', self.name)
        print('Color:',self.color)
        print('Weight:',self.weight)

R=Robot()
R.setName("Tom")
R.setColor("Red")
R.setWeight(55)
R.display()