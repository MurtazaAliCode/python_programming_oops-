class car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def display(self):
        return f"Model: {self.model}, Year: {self.year}"

car1 = car("BMW", 2020)
print(car1.display())
      
    