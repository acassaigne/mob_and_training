class ShoppingCart:

    def __init__(self):
        self.prices_of_items = []

    def add(self, price):
        self.prices_of_items.append(price)

    def calculate_total_price(self):
        return sum(self.prices_of_items)

    def has_discount(self):
        result = [item_price >= 100 for item_price in self.prices_of_items]
        return any(result)

    def number_of_products(self):
        return len(self.prices_of_items)


class SomeConsumer():
    def do_stuff():
        shoppingCart = ShoppingCart()
        shoppingCart.add(100)
        print("other consumer", shoppingCart.calculate_total_price())


if __name__ == "__main__":
    shoppingCart = ShoppingCart()
    shoppingCart.add(10)
    print("number of products:", shoppingCart.number_of_products())
    print("total price:", shoppingCart.calculate_total_price())
    print("has discount:", shoppingCart.has_discount())
