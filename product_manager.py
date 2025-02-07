from product import Product

class ProductManager:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
        
    def display_all_products(self):
        for product in self.products:
            product.display_info()
         
    def total_sum(self):
        ukupno = sum(product.price * product.quantity for product in self.products)
        print(f"Ukupna cena svih proizvoda je: {ukupno:.2f} dinara")