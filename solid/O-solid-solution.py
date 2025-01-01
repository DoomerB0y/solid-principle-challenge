from abc import ABC, abstractmethod

class FeeCalculator(ABC):

    @abstractmethod
    def fee(self, amount):
        pass

class CreditCard(FeeCalculator):
    def fee(self, amount):
        return amount * 0.03
    
class Paypal(FeeCalculator):
    def fee(self, amount):
        return amount * 0.05

class BankTransfer(FeeCalculator):
    def fee(self, amount):
        return 2.50
    
class UnknownMethod(FeeCalculator):
    def fee(self, amount):
        return amount * 0.0