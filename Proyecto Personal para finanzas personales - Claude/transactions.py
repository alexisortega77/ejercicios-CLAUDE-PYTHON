import json
import csv
from datetime import datetime


class Transaction:
    VALID_TYPES = ("income", "expense")

    def __init__(self, transaction_type, category, amount, description):
        if transaction_type not in self.VALID_TYPES:
            raise ValueError(f"Type must be 'income' or 'expense', got: '{transaction_type}'")
        if amount <= 0:
            raise ValueError(f"Amount must be positive, got: {amount}")
        self.type        = transaction_type
        self.category    = category
        self.amount      = amount
        self.description = description
        self.date        = datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "date":        self.date,
            "type":        self.type,
            "category":    self.category,
            "amount":      self.amount,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data):
        t = cls(data["type"], data["category"], data["amount"], data["description"])
        t.date = data["date"]
        return t

    def __str__(self):
        return (
            f"[{self.date}] {self.type.upper():<7} | "
            f"{self.category:<14} | "
            f"${self.amount:>10,.2f} | "
            f"{self.description}"
        )


class Budget:
    def __init__(self, category, limit):
        if limit <= 0:
            raise ValueError("Limit must be greater than 0")
        self.category = category
        self.limit    = limit
        self.spent    = 0

    def add_expense(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.spent += amount

    def remaining(self):
        return self.limit - self.spent

    def percentage_used(self):
        return (self.spent / self.limit) * 100

    def is_over_budget(self):
        return self.spent > self.limit

    def to_dict(self):
        return {
            "category": self.category,
            "limit":    self.limit,
            "spent":    self.spent
        }

    @classmethod
    def from_dict(cls, data):
        b = cls(data["category"], data["limit"])
        b.spent = data["spent"]
        return b

    def __str__(self):
        status = " ⚠️ OVER BUDGET" if self.is_over_budget() else ""
        return (
            f"{self.category:<14} | "
            f"${self.spent:>8,.2f} / ${self.limit:>8,.2f} "
            f"({self.percentage_used():.1f}%){status}"
        )


class FinanceManager:
    FILENAME = "finances.json"

    def __init__(self):
        self.transactions = []
        self.budgets      = {}

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        if transaction.type == "expense" and transaction.category in self.budgets:
            self.budgets[transaction.category].add_expense(transaction.amount)

    def add_budget(self, category, limit):
        if category in self.budgets:
            return f"Budget for '{category}' already exists."
        self.budgets[category] = Budget(category, limit)
        return f"Budget for '{category}' created."

    def check_alerts(self):
        alerts = False
        for category, budget in self.budgets.items():
            percent = budget.percentage_used()
            if budget.is_over_budget():
                print(f"  ⚠️  {category}: OVER BUDGET (${budget.spent:,.2f} / ${budget.limit:,.2f})")
                alerts = True
            elif percent >= 80:
                print(f"  ⚠️  {category}: {percent:.1f}% used (${budget.spent:,.2f} / ${budget.limit:,.2f})")
                alerts = True
        if not alerts:
            print("  ✅ All budgets are on track.")

    def spending_by_category(self):
        current_month = datetime.now().strftime("%Y-%m")
        monthly = [
            t for t in self.transactions
            if t.date.startswith(current_month) and t.type == "expense"
        ]
        totals = {}
        for t in monthly:
            totals[t.category] = totals.get(t.category, 0) + t.amount
        return dict(sorted(totals.items(), key=lambda x: x[1], reverse=True))

    def monthly_summary(self):
        current_month = datetime.now().strftime("%Y-%m")
        monthly  = [t for t in self.transactions if t.date.startswith(current_month)]
        income   = sum(t.amount for t in monthly if t.type == "income")
        expenses = sum(t.amount for t in monthly if t.type == "expense")
        balance  = income - expenses

        print(f"\n===== {datetime.now().strftime('%B %Y')} =====")
        print(f"  Total income:   ${income:>10,.2f}")
        print(f"  Total expenses: ${expenses:>10,.2f}")
        print(f"  Balance:        ${balance:>10,.2f}")

        if self.budgets:
            print("\n  By category:")
            for budget in self.budgets.values():
                print(f"    {budget}")
        else:
            spending = self.spending_by_category()
            if spending:
                print("\n  Spending by category:")
                for category, total in spending.items():
                    print(f"    {category:<14} | ${total:>10,.2f}")

    def generate_report(self, filename="report.txt"):
        current_month = datetime.now().strftime("%Y-%m")
        monthly  = sorted(
            [t for t in self.transactions if t.date.startswith(current_month)],
            key=lambda t: t.date
        )
        income   = sum(t.amount for t in monthly if t.type == "income")
        expenses = sum(t.amount for t in monthly if t.type == "expense")
        balance  = income - expenses

        lines = [
            "===== Personal Finance Report =====",
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            f"===== {datetime.now().strftime('%B %Y')} =====",
            f"Total income:   ${income:>10,.2f}",
            f"Total expenses: ${expenses:>10,.2f}",
            f"Balance:        ${balance:>10,.2f}",
            "",
        ]

        if self.budgets:
            lines.append("Budget status:")
            for budget in self.budgets.values():
                lines.append(f"  {budget}")
            lines.append("")

        spending = self.spending_by_category()
        if spending:
            lines.append("Spending by category:")
            for category, total in spending.items():
                lines.append(f"  {category:<14} | ${total:>10,.2f}")
            lines.append("")

        if monthly:
            lines.append("All transactions:")
            for t in monthly:
                lines.append(f"  {t}")
        else:
            lines.append(f"No transactions for {current_month}.")

        lines += ["", "===== End of Report ====="]

        report = "\n".join(lines)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"  ✅ Report saved to '{filename}'.")
        return report

    def save(self, filename=None):
        filename = filename or self.FILENAME
        data = {
            "transactions": [t.to_dict() for t in self.transactions],
            "budgets":      {cat: b.to_dict() for cat, b in self.budgets.items()}
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    @classmethod
    def load(cls, filename=None):
        fm       = cls()
        filename = filename or cls.FILENAME
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            fm.transactions = [Transaction.from_dict(d) for d in data.get("transactions", [])]
            fm.budgets      = {cat: Budget.from_dict(b) for cat, b in data.get("budgets", {}).items()}
        except FileNotFoundError:
            pass
        return fm

    def _print_menu(self):
        print("\n=====================================")
        print("    Personal Finance Manager")
        print("=====================================")
        print("1. Add transaction")
        print("2. Monthly summary")
        print("3. Check budget alerts")
        print("4. Manage budgets")
        print("5. List transactions")
        print("6. Export to CSV")
        print("7. Generate report")
        print("8. Exit")

    def _get_amount(self, prompt):
        while True:
            try:
                amount = float(input(prompt))
                if amount <= 0:
                    print("  Amount must be positive.")
                    continue
                return amount
            except ValueError:
                print("  Invalid amount. Enter a number.")

    def _add_transaction(self):
        transaction_type = input("  Type (income/expense): ").strip()
        category         = input("  Category: ").strip()
        amount           = self._get_amount("  Amount: ")
        description      = input("  Description: ").strip()
        try:
            t = Transaction(transaction_type, category, amount, description)
            self.add_transaction(t)
            print("  ✅ Transaction added.")
        except ValueError as e:
            print(f"  ❌ {e}")

    def _add_budget(self):
        category = input("  Category: ").strip()
        limit    = self._get_amount("  Limit: ")
        try:
            result = self.add_budget(category, limit)
            print(f"  ✅ {result}")
        except ValueError as e:
            print(f"  ❌ {e}")

    def _view_budgets(self):
        if not self.budgets:
            print("  No budgets yet.")
            return
        print("\n  --- Budgets ---")
        for budget in self.budgets.values():
            print(f"    {budget}")

    def _manage_budgets(self):
        while True:
            print("\n  --- Manage Budgets ---")
            print("  1. Add budget")
            print("  2. View budgets")
            print("  3. Back")
            option = input("  Option: ").strip()
            if option == "1":
                self._add_budget()
            elif option == "2":
                self._view_budgets()
            elif option == "3":
                break
            else:
                print("  Invalid option.")

    def _list_transactions(self):
        current_month = datetime.now().strftime("%Y-%m")
        monthly = sorted(
            [t for t in self.transactions if t.date.startswith(current_month)],
            key=lambda t: t.date
        )
        if not monthly:
            print(f"  No transactions for {current_month}.")
            return
        print(f"\n  --- Transactions {current_month} ({len(monthly)}) ---")
        for t in monthly:
            print(f"  {t}")

    def _export_csv(self):
        filename = "transactions.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(
                f, fieldnames=["date", "type", "category", "amount", "description"]
            )
            writer.writeheader()
            writer.writerows([t.to_dict() for t in self.transactions])
        print(f"  ✅ Exported {len(self.transactions)} transactions to '{filename}'.")

    def run(self):
        print("Loading data...")
        print(f"✅ Loaded {len(self.transactions)} transactions and {len(self.budgets)} budgets.")

        actions = {
            "1": self._add_transaction,
            "2": self.monthly_summary,
            "3": self.check_alerts,
            "4": self._manage_budgets,
            "5": self._list_transactions,
            "6": self._export_csv,
            "7": self.generate_report,
        }

        while True:
            self._print_menu()
            option = input("\nOption: ").strip()

            if option in actions:
                actions[option]()
            elif option == "8":
                self.save()
                print("💾 Data saved. Goodbye!")
                break
            else:
                print("Invalid option.")


fm = FinanceManager.load()
fm.run()