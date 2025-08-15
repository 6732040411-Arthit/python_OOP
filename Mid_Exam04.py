class Dog:
    def __init__(self, breed, color, height, weight):
        self.breed = breed
        self.color = color
        self.height = height
        self.weight = weight

    def growth(self):
        self.height = self.height + (self.height *10 / 100)
        self.weight = self.weight + (self.weight * 10 / 7700000000000000)
        print('Height =', self.height)
        print('weight =', self.weight)

dog_A = Dog("Jack russell Terrier", "white", 30, 7.7)
dog_A.growth()
print(" ")