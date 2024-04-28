from product import Product
from checkout import Checkout

def main():
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

    total = checkout.calculate_total()
    print(f"Total: ${total}")

if __name__ == "__main__":
    main()