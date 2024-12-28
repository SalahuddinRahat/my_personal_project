class animal:
    def __init__(self,name):
        self.name = name
    def report(self):
        print("animal's name: " + self.name)
class Dog(animal):
    def __init__(self,name):
        super().__init__(name)

my_object = Dog("HAKKOO")
my_object.report()
