class NegativeAmountError(Exception):
    pass


class InsufficientBalanceError(Exception):
    pass


class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def _validate_amount(self, amount: float):
        if amount <= 0:
            raise NegativeAmountError(f"Amount must be greater than 0: {amount}")

    def deposit(self, amount: float):
        self._validate_amount(amount)
        self.balance += amount

        self.history.append({
            "type": "deposit",
            "amount": amount,
            "balance_after": self.balance
        })

        return self.balance

    def withdraw(self, amount: float):
        self._validate_amount(amount)

        if amount > self.balance:
            raise InsufficientBalanceError(
                f"Insufficient balance. Current balance: {self.balance}"
            )

        self.balance -= amount

        self.history.append({
            "type": "withdraw",
            "amount": amount,
            "balance_after": self.balance
        })

        return self.balance

    def get_account_summary(self):
        return {
            "owner": self.owner,
            "balance": self.balance,
            "history": self.history
        }


# 🔵 Nueva clase
class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: float = 0, interest_rate: float = 0.10):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount

        self.history.append({
            "type": "interest",
            "amount": interest_amount,
            "balance_after": self.balance
        })

        return self.balance
account = SavingsAccount("Alexis", 1000)

try:
        account.deposit(500)
        account.withdraw(200)
        account.apply_interest()
        account.withdraw(2000)  # Esto debe fallar
except (NegativeAmountError, InsufficientBalanceError) as e:
        print(f"Error: {e}")
summary = account.get_account_summary()
print(summary)