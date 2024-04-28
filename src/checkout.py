class Checkout:
    def __init__(self, products):
        self.products = products
        self.cart = {}

    def scan(self, product_code, quantity=1):
        if product_code in self.cart:
            self.cart[product_code] += quantity
        else:
            self.cart[product_code] = quantity

    def calculate_total(self):
        total = 0
        for product_code, quantity in self.cart.items():
            product = self.products.get(product_code)
            if product:
                if product.special_price.keys():
                    special_price = product.special_price.get(min(product.special_price.keys()), None)
                    if special_price is not None:
                        items_for_discount = min(product.special_price.keys())
                        while quantity - items_for_discount >= 0:
                            
                            total += special_price
                            quantity -= items_for_discount
                total += quantity * product.unit_price
        return total
