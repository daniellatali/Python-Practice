## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## dog is a class where it has __init__ and it takes the self and name values
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## cat is a class that also has __init__ and takes self and name values
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## person is a class that also has __init__ and takes name and self values
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? Hmm what is this strange magic? <-- Calls for data or values from subclasses
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(Animal):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## Rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat
satan = Cat("Satan")

## Mary is-a person
mary = Person("Mary")

## Mary has-a cat named satan
mary.pet = Satan

## Frank is-a Employee whose name is Frank and has salary of 120000
frank = Employee("Frank", 120000)

## Frank has-a pet named Rover
frank.pet = Rover

## Flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## Harry is-a Halibut
harry = Halibut()
