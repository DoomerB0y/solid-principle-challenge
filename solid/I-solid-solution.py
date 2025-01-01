from abc import ABC, abstractmethod

class PayService(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

class RefundService(ABC):
    @abstractmethod
    def refund(self, amount: float) -> None:
        pass

class DisputeService(ABC):
    @abstractmethod
    def handle_dispute(self, dispute_id: str) -> None:
        pass

class BasicGiftCard(PayService):
    def pay(self, amount: float) -> None:
        return print(f"Gift card used to pay {amount}.")

class StandartGiftCard(PayService, RefundService):
    def pay(self, amount: float) -> None:
        return print(f"Gift card used to pay {amount}.")

    def refund(self, amount: float) -> None:
        return print(f"Gift card refund {amount}.")

class PremiunGiftCard(PayService, RefundService, DisputeService ):
    def pay(self, amount: float) -> None:
        print(f"Gift card used to pay {amount}.")

    def refund(self, amount: float) -> None:
        return print(f"Gift card refund {amount}.")
    
    def handle_dispute(self, dispute_id: str) -> None:
        return print(f"This Gift card is in dispute: Dispute ID: {dispute_id}")