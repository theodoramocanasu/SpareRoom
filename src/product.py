
class Product:
    def __init__(self, code, unit_price, special_price=None):
        self.code = code
        self.unit_price = unit_price
        self.special_price = special_price if special_price else {}

    def __str__(self):
        return f"{self.code} - ${self.unit_price}"