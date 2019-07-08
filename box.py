
class Box:

    def __init__(self, id, capacity):
        self.id = id
        self.dogs = []
        self.capacity = capacity

    @property
    def status(self):
        return len(self.dogs)

    def add_dog(self, dog):
        if self.capacity > self.status:
            self.dogs.append(dog)
            return True
        else:
            return False

    def remove_dog(self, dog):
        if self.status > 0:
            self.dogs.remove(dog)
            return True
        else:
            return False
