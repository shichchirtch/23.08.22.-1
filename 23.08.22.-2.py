class Body:

    def __init__(self, name, ro, volume):
        if isinstance(name, str):
            self.name = name
        if type(ro) in (int, float) and type(volume) in (int, float):
            self.ro = ro
            self.volume = volume

    def __eq__(self, other):
        if isinstance(other, Body):
            return True if self.ro*self.volume == other.ro*other.volume else False
        if type(other) in (int, float):
            return True if self.ro*self.volume == other else False
    def __lt__(self, other):
        if isinstance(other, Body):
            return True if self.ro*self.volume < other.ro*other.volume else False
        if type(other) in (int, float):
            return True if self.ro*self.volume < other else False
    def __gt__(self, other):
        if isinstance(other, Body):
            return True if self.ro*self.volume > other.ro*other.volume else False
        if type(other) in (int, float):
            return True if self.ro*self.volume > other else False


body1=Body("first", 10, 3)
body2=Body("second", 10, 3)

# print(body1 < 31)  # True, если масса тела body1 больше массы тела body2
# print(body1 == 30) # True, если масса тела body1 равна массе тела body2
print(body1 < 40)     # True, если масса тела body1 меньше 10
# body2 == 5     # True, если масса тела body2 равна 5
