from promotions import Promotion
import math

class Product:
    def __init__(self, name="", price=0.0, quantity=1, promotions:list[Promotion]=[]) -> None:
        if (len(name) < 1):
            raise ValueError("Empty name")

        self.quantity = quantity
        self.name = name
        self.price = price
        self.active = True
        self.promotions = promotions

    def __del__(self) -> None:
        pass

    def get_quantity(self) -> float:
        return self.quantity
    
    def set_quantity(self, quantity) -> None:
        self.quantity = quantity

    def is_active(self) -> bool:
        return self.active
    
    def activate(self) -> None:
        self.active = True

    def deactivate(self) -> None:
        self.active = False

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, {self.get_promotions_display()}"
    
    def buy(self, quantity) -> float:
        self.quantity = max(self.quantity - quantity, 0)
        
        if self.quantity <= 0:
            self.deactivate()

        total_discount = math.prod([prom.apply_promotion(quantity) for prom in self.promotions]) if len(self.promotions) > 0 else 1

        return self.price * quantity * total_discount
    
    def get_promotions_display(self) -> str:
        return ", ".join([prom.title for prom in self.promotions])
    
class NonStockedProduct(Product):
    def __init__(self, name="", price=0, quantity=1) -> None:
        super().__init__(name, price, 0)

    def set_quantity(self, quantity) -> None:
        pass

    def deactivate(self) -> None:
        pass

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: Unlimited, {self.get_promotions_display()}"

class LimitedProduct(Product):
    def __init__(self, name="", price=0, quantity=1, maximum=1) -> None:
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Limited to 1 per order!, {self.get_promotions_display()}"