class Device:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def re_sale(self):
        print('ready to sell again')


class Laptop(Device):
    def __init__(self, brand, price, color, disc_size):

        super().__init__(brand, price, color)

        self.disc_size = disc_size

    def run(self):
        print('running the laptop')

    def __repr__(self) -> str:
        return f'Laptop {self.brand} :{self.price} :{self.color}'


lenovo = Laptop('Lenovo', 42000, 'black', '500gb')
hp = Laptop('HP', 35000, 'silver', '250gb')

print(lenovo)
print(hp)

hp.re_sale()
print(hp.brand)
