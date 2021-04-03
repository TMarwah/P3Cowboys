# create Class
class Person:
    def __init__(self, name, age, sport):
        self.name = name
        self.age = age
        self.sport = sport

    def Person1(self):
        print("Hello my name is " + self.name, "I like to play" + self.sport)

    def Person2(self):
        print("Hello my name is " + self.name, "I like to play" + self.sport)

    def Person3(self):
        print("Hello my name is " + self.name, "I like to" + self.sport)

    def Person4(self):
        print("Hello my name is " + self.name, "I like to play" + self.sport)

    def Person5(self):
        print("Hello my name is " + self.name, "and I like to eat" + self.sport)

    @property
    def Name(self):
        return self.name

    @property
    def Age(self):
        return self.age

    @property
    def Sport(self):
        return self.sport


p1 = Person("Billy", 17, " Soccer")
p1.Person1()
p2 = Person("Marc", 17, " Basketball")
p2.Person2()
p3 = Person("Karam", 17, " Code")
p3.Person3()
p4 = Person("Allen", 17, " Fortnite")
p4.Person4()
p5 = Person("Tanmmay", 17, " food")
p5.Person5()
