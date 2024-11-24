from abc import ABC, abstractclassmethod


class DiscountCalculator(ABC):
    @abstractclassmethod
    def get_discounted_product(self):
        pass


class DiscountCalculatorShirt(DiscountCalculator):
    def __init__(self, cost):
        self.cost = cost

    def get_discounted_product(self):
        return self.cost - (self.cost * 0.10)


class DiscountCalculatorTshirt(DiscountCalculator):
    def __init__(self, cost):
        self.cost = cost

    def get_discounted_product(self):
        return self.cost - (self.cost * 0.15)


class DiscountCalculatorPant(DiscountCalculator):
    def __init__(self, cost):
        self.cost = cost

    def get_discounted_product(self):
        return self.cost - (self.cost * 0.20)


dc_shirt = DiscountCalculatorShirt(100)
print(dc_shirt.get_discounted_product())

dc_tshirt = DiscountCalculatorTshirt(1000)
print(dc_tshirt.get_discounted_product())

dc_pant = DiscountCalculatorPant(500)
print(dc_pant.get_discounted_product())
