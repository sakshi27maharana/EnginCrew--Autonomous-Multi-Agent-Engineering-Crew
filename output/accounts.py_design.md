# Account Management System
The account management system will be implemented in a single Python module named `accounts.py`. The module will contain a single class `Account` that will manage the user's account and provide methods for depositing funds, withdrawing funds, buying and selling shares, and reporting the user's holdings and profit/loss.

## Class: Account
### Description
The `Account` class represents a user's account in the trading simulation platform. It provides methods for managing the user's account, including depositing funds, withdrawing funds, buying and selling shares, and reporting the user's holdings and profit/loss.

### Attributes
* `balance`: The user's current balance.
* `holdings`: A dictionary where the keys are the share symbols and the values are the quantities of each share.
* `transactions`: A list of transactions made by the user.
* `initial_deposit`: The user's initial deposit.

### Methods
#### `__init__(initial_deposit)`
* Initializes a new `Account` object with the given `initial_deposit`.
* Sets the `balance` to the `initial_deposit`.
* Initializes an empty `holdings` dictionary.
* Initializes an empty `transactions` list.

#### `deposit(amount)`
* Deposits the given `amount` into the user's account.
* Updates the `balance` by adding the `amount`.
* Appends a deposit transaction to the `transactions` list.

#### `withdraw(amount)`
* Withdraws the given `amount` from the user's account.
* Checks if the withdrawal would result in a negative balance. If so, raises a `ValueError`.
* Updates the `balance` by subtracting the `amount`.
* Appends a withdrawal transaction to the `transactions` list.

#### `buy(symbol, quantity)`
* Buys the given `quantity` of shares with the given `symbol`.
* Gets the current price of the share using the `get_share_price` function.
* Calculates the total cost of the shares.
* Checks if the user has sufficient funds to buy the shares. If not, raises a `ValueError`.
* Updates the `balance` by subtracting the total cost.
* Updates the `holdings` dictionary by adding the `quantity` to the existing quantity of the share.
* Appends a buy transaction to the `transactions` list.

#### `sell(symbol, quantity)`
* Sells the given `quantity` of shares with the given `symbol`.
* Checks if the user has sufficient shares to sell. If not, raises a `ValueError`.
* Gets the current price of the share using the `get_share_price` function.
* Calculates the total revenue from the sale.
* Updates the `balance` by adding the total revenue.
* Updates the `holdings` dictionary by subtracting the `quantity` from the existing quantity of the share.
* Appends a sell transaction to the `transactions` list.

#### `get_holdings()`
* Returns the user's current holdings as a dictionary.

#### `get_balance()`
* Returns the user's current balance.

#### `get_profit_loss()`
* Calculates the profit/loss by subtracting the `initial_deposit` from the current `balance` and adding the value of the user's holdings.
* Returns the profit/loss.

#### `get_transactions()`
* Returns the list of transactions made by the user.

## Function: get_share_price(symbol)
### Description
The `get_share_price` function returns the current price of a share with the given `symbol`.
### Test Implementation
A test implementation of the `get_share_price` function will be provided that returns fixed prices for AAPL, TSLA, and GOOGL.

## Example Use Cases
```python
account = Account(1000)
account.deposit(500)
account.buy("AAPL", 10)
account.sell("AAPL", 5)
print(account.get_holdings())
print(account.get_balance())
print(account.get_profit_loss())
print(account.get_transactions())
```
