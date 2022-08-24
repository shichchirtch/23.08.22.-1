class MoneyR:
    def __init__(self, balance=0.0):
        self._volume = balance
        self._cb = None
        self.type_money = "rub"

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value

    @property
    def cb(self):
        return self._cb

    @cb.setter
    def cb(self, balance):
        self._cb = balance

    def __eq__(self, other):
        if self._cb is None:
            raise ValueError("Кошелёк не зарегистрирован")
        if self._cb is None:
            raise ValueError("Неизвестен курс валют.")
        if type(other) in (MoneyR, MoneyD, MoneyE):
            v1 = self.volume/CentralBank.rates[self.type_money]
            v2 = other.volume/CentralBank.rates[other.type_money]
            return True if abs(v1 - v2) <= 0.001 else False

    def __lt__(self, other):
        if self._cb is None:
            raise ValueError("Кошелёк не зарегистрирован")
        if self._cb is None:
            raise ValueError("Неизвестен курс валют.")
        if type(other) in (MoneyR, MoneyD, MoneyE):
            v1 = self.volume/self.cb.rates[self.type_money]
            v2 = other.volume/other.cb.rates[other.type_money]
            return True if v1 - v2 < 0.1 else False

    def __le__(self, other):
        if self._cb is None:
            raise ValueError("Кошелёк не зарегистрирован")
        if self._cb is None:
            raise ValueError("Неизвестен курс валют.")
        if type(other) in (MoneyR, MoneyD, MoneyE):
            v1 = self.volume/self.cb.rates[self.type_money]
            v2 = other.volume/other.cb.rates[other.type_money]
            return True if abs(v1 - v2) <= 0.1 else False
    def __gt__(self, other):
        if self._cb is None:
            raise ValueError("Кошелёк не зарегистрирован")
        if self._cb is None:
            raise ValueError("Неизвестен курс валют.")
        if type(other) in (MoneyR, MoneyD, MoneyE):
            v1 = self.volume/self.cb.rates[self.type_money]
            v2 = other.volume/other.cb.rates[other.type_money]
            return True if v1 - v2 > 0.1 else False

    def __ge__(self, other):
        if self._cb is None:
            raise ValueError("Кошелёк не зарегистрирован")
        if self._cb is None:
            raise ValueError("Неизвестен курс валют.")
        if type(other) in (MoneyR, MoneyD, MoneyE):
            v1 = self.volume/self.cb.rates[self.type_money]
            v2 = other.volume/other.cb.rates[other.type_money]
            return True if abs(v1 - v2) >= 0.1 else False


class MoneyD:
    def __init__(self, balance=0.0):
        self._volume = balance
        self._cb = None
        self.type_money = "dollar"

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value

    @property
    def cb(self):
        return self._cb

    @cb.setter
    def cb(self, balance):
        self._cb = balance
    def __eq__(self, other):
        if self._cb is None:
            raise ValueError("Кошелёк не зарегистрирован")
        if self._cb is None:
            raise ValueError("Неизвестен курс валют.")
        if type(other) in (MoneyR, MoneyD, MoneyE):
            v1 = self.volume/CentralBank.rates[self.type_money]
            v2 = other.volume/CentralBank.rates[other.type_money]
            return True if abs(v1 - v2) <= 0.001 else False

    def __lt__(self, other):
        if self._cb is None:
            raise ValueError("Кошелёк не зарегистрирован")
        if self._cb is None:
            raise ValueError("Неизвестен курс валют.")
        if type(other) in (MoneyR, MoneyD, MoneyE):
            v1 = self.volume/self.cb.rates[self.type_money]
            v2 = other.volume/other.cb.rates[other.type_money]
            return True if v1 - v2 < 0.1 else False

    def __le__(self, other):
        if self._cb is None:
            raise ValueError("Кошелёк не зарегистрирован")
        if self._cb is None:
            raise ValueError("Неизвестен курс валют.")
        if type(other) in (MoneyR, MoneyD, MoneyE):
            v1 = self.volume/self.cb.rates[self.type_money]
            v2 = other.volume/other.cb.rates[other.type_money]
            return True if abs(v1 - v2) <= 0.1 else False
    def __gt__(self, other):
        if self._cb is None:
            raise ValueError("Кошелёк не зарегистрирован")
        if self._cb is None:
            raise ValueError("Неизвестен курс валют.")
        if type(other) in (MoneyR, MoneyD, MoneyE):
            v1 = self.volume/self.cb.rates[self.type_money]
            v2 = other.volume/other.cb.rates[other.type_money]
            return True if v1 - v2 > 0.1 else False

    def __ge__(self, other):
        if self._cb is None:
            raise ValueError("Кошелёк не зарегистрирован")
        if self._cb is None:
            raise ValueError("Неизвестен курс валют.")
        if type(other) in (MoneyR, MoneyD, MoneyE):
            v1 = self.volume/self.cb.rates[self.type_money]
            v2 = other.volume/other.cb.rates[other.type_money]
            return True if abs(v1 - v2) >= 0.1 else False


class MoneyE:
    def __init__(self, balance=0.0):
        self._volume = balance
        self._cb = None
        self.type_money = "euro"

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value

    @property
    def cb(self):
        return self._cb

    @cb.setter
    def cb(self, balance):
        self._cb = balance
    def __eq__(self, other):
        if self._cb is None:
            raise ValueError("Кошелёк не зарегистрирован")
        if self._cb is None:
            raise ValueError("Неизвестен курс валют.")
        if type(other) in (MoneyR, MoneyD, MoneyE):
            v1 = self.volume/CentralBank.rates[self.type_money]
            v2 = other.volume/CentralBank.rates[other.type_money]
            return True if abs(v1 - v2) <= 0.001 else False

    def __lt__(self, other):
        if self._cb is None:
            raise ValueError("Кошелёк не зарегистрирован")
        if self._cb is None:
            raise ValueError("Неизвестен курс валют.")
        if type(other) in (MoneyR, MoneyD, MoneyE):
            v1 = self.volume/self.cb.rates[self.type_money]
            v2 = other.volume/other.cb.rates[other.type_money]

            return True if v1 - v2 < 0.1 else False

    def __le__(self, other):
        if self._cb is None:
            raise ValueError("Кошелёк не зарегистрирован")
        if self._cb is None:
            raise ValueError("Неизвестен курс валют.")
        if type(other) in (MoneyR, MoneyD, MoneyE):
            v1 = self.volume/self.cb.rates[self.type_money]
            v2 = other.volume/other.cb.rates[other.type_money]
            return True if abs(v1 - v2) <= 0.1 else False
    def __gt__(self, other):
        if self._cb is None:
            raise ValueError("Кошелёк не зарегистрирован")
        if self._cb is None:
            raise ValueError("Неизвестен курс валют.")
        if type(other) in (MoneyR, MoneyD, MoneyE):
            v1 = self.volume/self.cb.rates[self.type_money]
            v2 = other.volume/other.cb.rates[other.type_money]
            return True if v1 - v2 > 0.1 else False

    def __ge__(self, other):
        if self._cb is None:
            raise ValueError("Кошелёк не зарегистрирован")
        if self._cb is None:
            raise ValueError("Неизвестен курс валют.")
        if type(other) in (MoneyR, MoneyD, MoneyE):
            v1 = self.volume/self.cb.rates[self.type_money]
            v2 = other.volume/other.cb.rates[other.type_money]
            return True if abs(v1 - v2) >= 0.1 else False


class CentralBank:
    def __new__(cls, *args, **kwargs):
        return None

    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    @classmethod
    def register(cls, money):
        money.cb = cls

print("*******************************************")
r = MoneyR(63.04)
d = MoneyD(1)
e = MoneyE(1)
a = CentralBank.register(r)
print("r.cb = ", a)
e.cb = CentralBank.register(e)

print("***", r == e)
