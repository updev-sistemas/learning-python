class Person :
    def __init__(self, name, email, phone, city) -> None:
        self.name = name
        self.email = email 
        self.phone = phone
        self.city = city
        pass

    def __eq__(self, __value) -> bool:
        if self.phone == __value.phone and self.email == __value.email:
            return True
        else :
            return False

    def __str__(self) -> str:
        return format("Nome = %s, Email = %s, Phone = %s, City = %s" % (self.name, self.email, self.phone, self.city))


if __name__ == '__main__' :

    antonio = Person(name = "Antonio Jose", email = "antonio@mail.a", phone = "(88) 9 9999-9999", city = "Quixeramobim")
    antonio2 = Person(name = "Antonio Jose", email = "antonio@mail.a", phone = "(88) 9 9999-9999", city = "Quixeramobim")
    naiara = Person(name = "Naiara", email = "naiara@mail.a", phone = "(88) 9 9999-9998", city = "Quixeramobim")

    print(antonio, '\n', naiara)

    if antonio == antonio2 :
        print('Sao iguais.')
    else:
        print('Sao diferentes')