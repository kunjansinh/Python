from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    def __init__(self, account_name):
        self.account_name = account_name

    @abstractmethod
    def process_payment(self, amount):
        pass


class CardPayment(PaymentMethod):
    def process_payment(self, amount):
        if amount <= 0:
            print("Payment amount must be positive.")
            return

        print(
            f"Card payment of £{amount:.2f} "
            f"processed for {self.account_name}."
        )


class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        if amount <= 0:
            print("Payment amount must be positive.")
            return

        print(
            f"PayPal payment of £{amount:.2f} "
            f"processed for {self.account_name}."
        )


def checkout(payment_method, amount):
    payment_method.process_payment(amount)


# Create payment objects
card = CardPayment("Alex")
paypal = PayPalPayment("Sam")

# Process payments
checkout(card, 49.99)
checkout(paypal, 25.50)

# Test invalid payment
checkout(card, -10)