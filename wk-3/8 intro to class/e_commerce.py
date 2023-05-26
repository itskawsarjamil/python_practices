class shopper:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        self.cart.append({'item': item, 'price': price, 'quantity': quantity})

    def checkout(self,amount):
        price=0
        for item in self.cart:
            print(item)
            price+=item['price']*item['quantity']
        print(price)

        if amount<price:
            return f"Amount need more {price-amount}"
        elif amount>price:
            return f"here are the items and extra money:{amount-price}"
        else:
            return f"items buying successfull"
        
my_shop=shopper('Kawsar')
my_shop.add_to_cart('shirt',1000,2)
my_shop.add_to_cart('shoe',2000,1)
my_shop.add_to_cart('pant',1200,2)
print(my_shop.cart)
reply=my_shop.checkout(6400)
print(reply)
