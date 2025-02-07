from product import Product
from product_manager import ProductManager

manager = ProductManager()

product1 = Product("Mouse", 1299, 12)
product2 = Product("Mixer", 2990, 25)
product3 = Product("Playstation4", 35000, 5)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

manager.display_all_products()

manager.total_sum()