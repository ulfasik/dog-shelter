
class Box:

    def __init__(self, id):
        self.id = id
        self.dogs = []

    def add_dog(self, dog):
        self.dogs.append(dog)

    def remove_dog(self, dog):
        self.dogs.remove(dog)
