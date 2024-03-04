class Property:
    def __init__(self, area: int, rooms: int, price: float, address: str) -> None:
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property(area={self.area}, rooms={self.rooms}, price={self.price}, address={self.address})"


class House(Property):

    def __init__(self, area: int, rooms: int, price: float, address: str, plot: int) -> None:
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House(plot={self.plot} extends {super().__str__()})"


class Flat(Property):
    def __init__(self, area: int, rooms: int, price: float, address: str, floor: int) -> None:
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat(floor={self.floor} extends {super().__str__()})"


if __name__ == '__main__':
    house = House(area=25, address="Katowice Bogucicka 10", rooms=4, price=700250, plot=10)
    flat = Flat(area=25, address="Katowice Bogucicka 6", rooms=3, price=500250, floor=3)
    print(house)
    print(flat)
