from abc import ABC, abstractmethod

class Promotion(ABC):
    @abstractmethod
    def apply_promotion(self, quantity):
        pass

class PercentagePromotion(Promotion):
    def __init__(self, percentage=1.0) -> None:
        self.percentage = percentage

    def apply_promotion(self, quantity) -> float:
        return self.percentage
    
class SecondItemPromotion(Promotion):
    def apply_promotion(self, quantity) -> float:
        return (quantity - 0.5) / quantity if quantity > 1 else 1.0
    
class BTGOF(Promotion):
    def apply_promotion(self, quantity) -> float:
        return (quantity - (quantity // 2)) / quantity