
box_numbers = [1, 2, 3]
dogs_allocation = [
    (1, "Ciapus"),
    (1, "Zuzia"),
    (1, "Robi"),
    (2, "Skrzypek"),
    (2, "Pimpus"),
    (3, "Nadi")
]  # This is an example for tuple


# Function is defined by 'def'
def is_allocated(dog, dogs_allocation):
    pass


class Shelter:

    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(self.name)
        print('-- PSY OBECNIE:')
        print(dogs)
        print('-- DOSTEPNE BOKSY')
        print(box_numbers)
        print('-- PRZYDZIAL PIESKOW')
        print(dogs_allocation)


class Dog:

    def __init__(self, name, sex, age, is_agressive):
        self.name = name
        self.sex = sex
        self.age = age
        self.is_agressive = is_agressive


class Box:

    def __init__(self, id):
        self.id = id
        self.dogs = []

    def add_dog(self, dog):
        self.dogs.append(dog)

    def remove_dog(self, dog):
        self.dogs.remove(dog)


# Main entry point is here
if __name__ == '__main__':
    #shelter = Shelter('PIESKOWY RAJ')
    #shelter.print_info()
    dog = Dog('Robi','male',2,True)
    dog2 = Dog('Zuzia','female', 4, False)

    box = Box(1)
    box.add_dog(dog)
    box.add_dog(dog2)
    print('in box {} there are {}'.format(box.id, box.dogs))
    box.remove_dog(dog)
    print('in box {} there are {}'.format(box.id, box.dogs))
    box.remove_dog(dog2)
    print('in box {} there are {}'.format(box.id, box.dogs))
