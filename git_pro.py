def hello():
    return('Hello dev!')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        print(f"Name of the person is {self.name} and age {self.age})