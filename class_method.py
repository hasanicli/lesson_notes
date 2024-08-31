class CartItem:
    discount_rate = 0.8

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

    @classmethod
    def set_discount_rate(cls, discount_rate):
        cls.discount_rate = discount_rate

    def apply_discount(self):
        self.price = self.price * self.discount_rate


if __name__ == '__main__':
    item1 = CartItem('apple', 5, 10)
    item1.set_discount_rate(1)
    item1.apply_discount()
    print(item1.calculate_total())

    item2 = CartItem('banana', 3, 7)
    item3 = CartItem('cherry', 6, 8)

    item2.apply_discount()
    result = item2.calculate_total()
    print(result)
