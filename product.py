class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def display_info(self):
        print(f"Informacije o proizvodu: Naziv: {self.name}, Cena: {self.price}, Količina: {self.quantity}")

        
    def azuriranje_poizvoda(self, nova_kolicina):
        if nova_kolicina >= 0:
            self.quantity = nova_kolicina
        else:
            print("Kolicina ne sme biti negativna")