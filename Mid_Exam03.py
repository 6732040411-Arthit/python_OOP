class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def new_color(self, color):
        self.color = color

car_A = Car("Honda", "civic", "2019", "black")
car_A.new_color('Red')
print('color =', car_A.color)