from shelter import Shelter
from dog import Dog
from box import Box


# Main entry point is here
if __name__ == '__main__':
    shelter = Shelter('PIESKOWY RAJ')
    shelter.print_info()

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
