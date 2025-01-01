from abc import ABC, abstractmethod

class PaymentService(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class PayPalService(PaymentService):
    def pay(self, amount: float):
        print(f"Paying {amount} using PayPal...")

class PaymentProcessor:
    def __init__(self, payment_service: PaymentService):
        self.payment_service = payment_service

    def process_payment(self, amount: float) -> None:
        self.payment_service.pay(amount)