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
        print("Hello my name is " + self.name, ". I am",  self.age, "and I like to eat" + self.sport)


p1 = Person("Billy", 17, " Soccer")
p1.Person1()
p1 = Person("Marc", 17, " Basketball")
p1.Person1()
p3 = Person("Karam", 17, " Code")
p3.Person3()
p1 = Person("Allen", 17, " Fortnite")
p1.Person1()
p5 = Person("Tanmmay", 17, " Food")
p5.Person5()
