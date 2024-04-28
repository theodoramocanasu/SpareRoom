import unittest
from src.product import Product
from src.checkout import Checkout

class TestCheckout(unittest.TestCase):
    def test_calculate_total(self):
        products = {
            "A": Product("A", 50, {3: 140}),
            "B": Product("B", 35, {2: 60}),
            "C": Product("C", 25),
            "D": Product("D", 12)
        }
        checkout = Checkout(products)
        checkout.scan("A", 3)
        checkout.scan("B", 3)
        checkout.scan("C", 1)
        checkout.scan("D", 2)

        self.assertEqual(checkout.calculate_total(), 284)

if __name__ == '__main__':
    unittest.main()
