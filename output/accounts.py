import datetime

class Account:
    def __init__(self, initial_deposit):
        self.balance = initial_deposit
        self.holdings = {}
        self.transactions = []
        self.initial_deposit = initial_deposit

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append({'type': 'deposit', 'amount': amount, 'timestamp': datetime.datetime.now()})

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('Insufficient funds')
        self.balance -= amount
        self.transactions.append({'type': 'withdrawal', 'amount': amount, 'timestamp': datetime.datetime.now()})

    def buy(self, symbol, quantity):
        price = get_share_price(symbol)
        total_cost = price * quantity
        if total_cost > self.balance:
            raise ValueError('Insufficient funds')
        self.balance -= total_cost
        if symbol in self.holdings:
            self.holdings[symbol] += quantity
        else:
            self.holdings[symbol] = quantity
        self.transactions.append({'type': 'buy', 'symbol': symbol, 'quantity': quantity, 'price': price, 'timestamp': datetime.datetime.now()})

    def sell(self, symbol, quantity):
        if symbol not in self.holdings or self.holdings[symbol] < quantity:
            raise ValueError('Insufficient shares')
        price = get_share_price(symbol)
        total_revenue = price * quantity
        self.balance += total_revenue
        self.holdings[symbol] -= quantity
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]
        self.transactions.append({'type': 'sell', 'symbol': symbol, 'quantity': quantity, 'price': price, 'timestamp': datetime.datetime.now()})

    def get_holdings(self):
        return self.holdings

    def get_balance(self):
        return self.balance

    def get_profit_loss(self):
        portfolio_value = self.balance
        for symbol, quantity in self.holdings.items():
            portfolio_value += quantity * get_share_price(symbol)
        return portfolio_value - self.initial_deposit

    def get_transactions(self):
        return self.transactions

def get_share_price(symbol):
    # Test implementation, returns fixed prices for AAPL, TSLA, and GOOGL
    prices = {'AAPL': 150.0, 'TSLA': 2000.0, 'GOOGL': 3000.0}
    return prices.get(symbol, 0.0)

# Example usage
account = Account(1000)
account.deposit(500)
account.buy('AAPL', 10)
account.sell('AAPL', 5)
print(account.get_holdings())
print(account.get_balance())
print(account.get_profit_loss())
print(account.get_transactions())
