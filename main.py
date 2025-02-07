from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

product1 = Product("Mouse", 1299, 12)
product2 = Product("Mixer", 2990, 25)
product3 = Product("Playstation4", 35000, 5)
product4 = Product("Ball", 250, 25)
product5 = Product("NoteBook", 100, 120)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)
manager.add_product(product4)
manager.add_product(product5)

manager.display_all_products()

manager.total_sum()

korpa = Cart()

korpa.add_product_cart(product4)
korpa.add_product_cart(product2)
korpa.add_product_cart(product1)

korpa.total_for_pay()
