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