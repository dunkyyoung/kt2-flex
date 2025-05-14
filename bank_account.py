class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Приватное поле

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

if __name__ == "__main__":
    account = BankAccount("Ivan", 1000)
    account.deposit(500)
    account.withdraw(200)
    print("Баланс:", account.get_balance())  # Ожидается: 1300
