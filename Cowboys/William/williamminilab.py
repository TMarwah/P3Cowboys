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


class Animal:
    def __init__(self, animal, name):
        self._animal = animal
        self._name = name

    @property
    def animal(self):
        return self._animal

    @property
    def name(self):
        return self._name

    @property
    def print(self):
        return self._name + ' ' + self._animal


if __name__ == "__main__":
    animals = [Animal('Dog', 'Yorky'), Animal('Dog', 'Weiner'), Animal('Dog', 'Pug'), Animal('Cat', 'Tom')]
    for animal in animals:
        print(animal.print)


