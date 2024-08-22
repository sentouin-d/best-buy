from products import Product

class Store:
    def __init__(self, initial_products:list[Product]) -> None:
        self.products = initial_products

    def add_product(self, product:Product) -> None:
        self.products.append(product)

    def remove_product(self, product:Product) -> None:
        try:
            self.products.remove(product)
        except ValueError as err:
            raise err
        
    def get_total_quantity(self) -> int:
        return sum([prod.get_quantity() for prod in self.products])
    
    def get_all_products(self) -> list[Product]:
        return [prod for prod in self.products if prod.is_active()]
    
    def order(self, shopping_list:list[tuple[Product, int]]) -> float:
        total = 0
        for item in shopping_list:
            total = total + item[0].buy(item[1])
        return total