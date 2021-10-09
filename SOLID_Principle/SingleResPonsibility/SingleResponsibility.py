class Cat:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def eat(self):
        print("eating")

    def walk(self):
        print("walking")

    def speak(self):
        print("speaking")

    """
    Cat은 먹고, 걷고, 말하는 동작을 한다. 하지만 이러한 속성들을 logging할 필요가 있을까?
    """
    # def repr(self):
    #     return f"name : {self.name}, age:{self.age}"

class Logger:
    def __init__(self, cat):
        self.cat = cat

    def __repr__(self) -> str:
        return f"name : {self.cat.name}, age:{self.cat.age}"

if __name__ == "__main__":
    chat = Cat(27, "ChaejinE")
    chat.eat()
    chat.walk()
    chat.speak()

    # Logging 기능이 필요하다면 Log를 담당하는 클래스를 만들어 사용하는 것이 좋다.
    logger = Logger(chat)
    print(logger)