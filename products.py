class Product:
    def __init__(self, name="", price=0.0, quantity=1) -> None:
        if (len(name) < 1):
            raise ValueError("Empty name")

        self.quantity = quantity
        self.name = name
        self.price = price
        self.active = True

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
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
    
    def buy(self, quantity) -> float:
        self.quantity = max(self.quantity - quantity, 0)
        
        if self.quantity <= 0:
            self.deactivate()
        
        return self.price * quantity
    
class NonStockedProduct(Product):
    def __init__(self, name="", price=0, quantity=1) -> None:
        super().__init__(name, price, 0)

    def set_quantity(self, quantity) -> None:
        pass

    def deactivate(self) -> None:
        pass

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: Unlimited"

class LimitedProduct(Product):
    def __init__(self, name="", price=0, quantity=1, maximum=1) -> None:
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Limited to 1 per order!"