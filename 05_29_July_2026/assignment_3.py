from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(PaymentStrategy):
    def pay(self, amount):
        discount = amount * 0.05   # 5% discount
        final_amount = amount - discount
        print(f"₹{final_amount:.2f} paid using Credit Card (5% discount applied).")


class PayPal(PaymentStrategy):
    def pay(self, amount):
        fee = 20   # Flat transaction fee
        final_amount = amount + fee
        print(f"₹{final_amount:.2f} paid using PayPal (₹20 fee added).")


class UPI(PaymentStrategy):
    def pay(self, amount):
        print(f"₹{amount:.2f} paid using UPI (No extra charges).")


class CryptoPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"₹{amount:.2f} paid using Cryptocurrency (BTC/ETH).")


class PaymentProcessor:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def process_payment(self, amount):
        self.payment_method.pay(amount)


amount = float(input("Enter Amount: ₹"))

print("\nChoose Payment Method")
print("1. Credit Card")
print("2. PayPal")
print("3. UPI")
print("4. Crypto")

choice = input("Enter Choice: ")

if choice == "1":
    payment = CreditCard()
elif choice == "2":
    payment = PayPal()
elif choice == "3":
    payment = UPI()
elif choice == "4":
    payment = CryptoPayment()
else:
    print("Invalid Choice")
    exit()

processor = PaymentProcessor(payment)
processor.process_payment(amount)




# #OUTPUT

# Enter Amount: ₹1000

# Choose Payment Method
# 1. Credit Card
# 2. PayPal
# 3. UPI
# 4. Crypto
# Enter Choice: 1

# ₹950.00 paid using Credit Card (5% discount applied).