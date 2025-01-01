from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    def __init__(self, balance: float):
        self.balance = balance

    @abstractmethod
    def pay(self, amount: float):
        pass

    @abstractmethod
    def pay(self, amount: float):
        pass

class RefundablePayment(PaymentMethod):

    def pay(self, amount: float):
        if amount > self.balance:
            print("Not enough balance.")
        else:
            self.balance -= amount
            print(f"[PaymentMethod] Paid {amount}. New balance: {self.balance}")

    def refund(self, amount: float):
            self.balance += amount
            print(f"[PaymentMethod] Refunded {amount}. New balance: {self.balance}")

class NonRefundablePayment(PaymentMethod):

    def pay(self, amount: float):
        if amount > self.balance:
            print("Not enough balance.")
        else:
            self.balance -= amount
            print(f"[PaymentMethod] Paid {amount}. New balance: {self.balance}")

    def refund(self, amount: float):
            return print("This Payment Method does not support refunds.")

