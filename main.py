from product import Product
from product_manager import ProductManager

manager = ProductManager()

product1 = Product("laptop", 98560, 3)
product2 = Product("PlayBox", 2700, 22)
product3 = Product("Trimer", 5500, 10)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)