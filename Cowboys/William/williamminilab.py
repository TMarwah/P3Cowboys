# create Class
class Person:
    def __init__(self, name, age, sport):
        self.name = name
        self.age = age
        self.sport = sport

    def Person1(self):
        print("Hello my name is " + self.name, ". I am", self.age, "and I like to play" + self.sport)

    def Person3(self):
        print("Hello my name is " + self.name, ". I am", self.age, "and I like to" + self.sport)

    def Person5(self):
        print("Hello my name is " + self.name, ". I am", self.age, "and I like to eat" + self.sport)


p1 = Person("Billy", 17, " Soccer")
p1.Person1()
p2 = Person("Marc", 17, " Basketball")
p2.Person1()
p1 = Person("Karam", 17, " Code")
p1.Person3()
p4 = Person("Allen", 17, " Fortnite")
p4.Person1()
p1 = Person("Tanmmay", 17, " Food")
p1.Person5()


class Exponent:
    def __init__(self, num1, num2):
        self.number_1 = num1
        self.number_2 = num2
        self.number_3 = self.number_1 ** self.number_2

    def dispanswers(self):
        return self.number_1, "^", self.number_2, "=", self.number_3

    def power(self):
        return self.number_1 ** self.number_2


class Dog:
    def setType1(self, t):
        self.type1 = t

    def getType1(self):
        return self.type1

    def setType2(self, t):
        self.type2 = t

    def getType2(self):
        return self.type2

    def setType3(self, t):
            self.type3 = t

    def getType3(self):
        return self.type3

    @property
    def display(self):
        return 'Type1:', self.type1, 'Type2:', self.type2, 'Type3:', self.type3


D = Dog()
D.setType1('Yorky')
D.setType2('Weiner dog')
D.setType3('Pug')

