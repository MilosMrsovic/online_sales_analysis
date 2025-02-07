from product import Product

class Cart:
    def __init__(self):
        self.cart = []
        
    def add_product_cart(self, product):
        self.cart.append(product)
        
    def total_for_pay(self):
        total = sum(product.price for product in self.cart)
        print(f"Ukupan iznos za naplatu u korpi je: {total:.2f} dinara")
        
    def display_cart_info(self):
          for product in self.cart:
              product.display_info()