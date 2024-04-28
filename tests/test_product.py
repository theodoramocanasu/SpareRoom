
import unittest
from src.product import Product

class TestProduct(unittest.TestCase):
    def test_product_str(self):
        product = Product("A", 50)
        self.assertEqual(str(product), "A - $50")

if __name__ == '__main__':
    unittest.main()