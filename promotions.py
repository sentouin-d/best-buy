from abc import ABC, abstractmethod

class Promotion(ABC):
    @abstractmethod
    def apply_promotion(self, quantity):
        pass

class PercentageDiscount(Promotion):
    def __init__(self, percentage=1.0) -> None:
        self.percentage = percentage
        self.title = f"{percentage * 100}% off!"

    def apply_promotion(self, quantity) -> float:
        return self.percentage
    
class SecondHalfPrice(Promotion):
    def __init__(self) -> None:
        self.title = "Second at Half Price!"

    def apply_promotion(self, quantity) -> float:
        return (quantity - 0.5) / quantity if quantity > 1 else 1.0
    
class SecondOneFree(Promotion):
    def __init__(self) -> None:
        self.title = "Second One Free!"

    def apply_promotion(self, quantity) -> float:
        return (quantity - (quantity // 2)) / quantity