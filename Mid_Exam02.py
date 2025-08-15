class Cashier:
    def __init__(self, products):
        self.products = products

    def recommend(self):
        products_string = " ".join(self.products)
        print(f"We have {products_string}")

cashier = Cashier(['apple', 'banana', 'orange.'])
cashier.recommend()