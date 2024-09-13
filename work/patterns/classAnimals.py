class animal:
    pass
class pet(animal):
    pass
class dog(pet):
    @staticmethod
    def bark():
        print("bow bow")

d = dog()
d.bark()