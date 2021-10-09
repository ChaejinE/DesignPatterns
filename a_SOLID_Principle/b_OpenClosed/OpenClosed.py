class Animal:
    def __init__(self, type):
        self.type = type

def hey(animal):
    if animal.type == "Cat":
        print("meow")

    elif animal.type == "Dog":
        print("bark")

chat_cat = Animal("Dog")
chat_dog = Animal("Cat")

hey(chat_cat)
hey(chat_dog)

"""
다른 동물(Sheep, Cow 등)이 들어왔을 때, hey함수는 수정이 필요해진다.
"""

class Animal:
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        print("meow")

class Dog(Animal):
    def speak(self):
        print("bark")

class Sheep(Animal):
    def speak(self):
        print("meh")

class Cow(Animal):
    def speak(self):
        print("moo")

def hey(animal):
    animal.speak()

chat_cat = Cat()
chat_dog = Dog()
chat_sheep = Sheep()
chat_cow = Cow()

hey(chat_cat)
hey(chat_dog)
hey(chat_sheep)
hey(chat_cow)

"""
Animal Class를 Abstract Class로 하여 Interface Method를 구현한다.
나머지 Class들은 이를 상속받아 부모의 Interface Method를 오버라이딩하여 
구현한다면, hey는 그 기능만을 사용하므로 수정의 필요성이 없어지게된다.
"""