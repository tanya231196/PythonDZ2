class Address:
    def __init__(self, index: int, city: str, street: str, house: int, flat: int):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.flat = flat

    def str(self):
        return str(self.index) + ", " + self.city + ", " + self.street + ", " + str(self.house) + " - " + str(self.flat) 
        
        