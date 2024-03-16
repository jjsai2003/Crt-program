class Order:
    def __init__(self, user, cart):
        self.user = user
        self.cart = cart

    def generate_bill(self):
        total = sum(product.price for product in self.cart.items)
        return total
