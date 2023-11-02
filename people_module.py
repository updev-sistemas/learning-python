class Person(object) :
    def __init__(self) -> None:
        self.name = ''
        pass

    def set_name(self, name) :
        self.name = name

    def get_name(self) :
        return self.name

class Customer(Person) :
    def __init__(self) -> None:
        Person.__init__(self)
        pass

class Supplier(Person) :
    def __init__(self) -> None:
        Person.__init__(self)
        pass

class Operator(Person) :
    def __init__(self) -> None:
        Person.__init__(self)
        pass