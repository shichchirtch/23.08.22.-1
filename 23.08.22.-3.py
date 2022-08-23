class Box:

    def __init__(self):
        self.box = []
    def add_thing(self, obj): #добавление предмета obj (объект другого класса Thing) в ящик;
        if isinstance(obj, Thing):
            self.box.append(obj)


    def get_things(self):
        return self.box

    def __eq__(self, other):
        if isinstance(other, Box):
            a = sorted(self.get_things(), key = lambda x: x.name)
            b = sorted(other.get_things(), key = lambda x: x.name)
            return True if a == b else False


class Thing:

    def __init__(self, name, mass):
        if isinstance(name, str):
            self.name = name
        if type(mass) in (int, float):
            self.mass = mass

    def __eq__(self, other):
        if isinstance(other, Thing):
            return True if self.name.lower() == other.name.lower() and self.mass==other.mass  else False



b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))
# b2.add_thing(Thing('доска2', 2000))
# print(b2.get_things())
# c = Thing('тряпка', 200)
# d = Thing('Тряпка', 200)
# print(c==d)
res = b1 == b2 # True
print(res)
