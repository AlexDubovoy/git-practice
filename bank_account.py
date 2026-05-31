class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        """Метод для вненсения денег на счет."""
        if amount > 0:
            self.__balance += amount
            print(f"Внесено {amount}. Новый баланс: {self.__balance}")
        else:
            print("Сумма депозита должна быть положительной!")

    def withdraw(self, amount):
        """Метод для снятия денег со счета."""
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Снято {amount}. Новый баланс: {self.__balance}")
            else:
                print("Недостаточно средств на счете!")
        else:
            print("Сумма снятия должна быть положительной!")

    def get_balance(self):
        """Метод доступа для получения баланса."""
        return self.__balance

    def set_balance(self, new_balance):
        """Метод доступа для установки баланса (для корректировки)."""
        if new_balance >= 0:
            self.__balance = new_balance
            print(f"Баланс установлен на {self.__balance}")
        else:
            print("Баланс не может быть отрицательным!")

account = BankAccount(1000)

account.deposit(500)
account.withdraw(200)
account.withdraw(2000)

print(f"Текущий баланс: {account.get_balance()}")

account.set_balance(5000)
print(f"Текущий баланс: {account.get_balance()}")
