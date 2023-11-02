from people_module import Person
from people_module import Supplier
from people_module import Customer
from people_module import Operator

def show_person(person) :
    print(person.get_name())

if __name__ == '__main__' :

    person1 = Supplier()
    person1.set_name('Distribuidora Uniao')

    person2 = Customer()
    person2.set_name('Antonio Jose')

    person3 = Operator()
    person3.set_name('Junior Lemos')
    
    show_person(person1)
    show_person(person2)
    show_person(person3)
