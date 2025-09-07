import gradio as gr
from accounts import Account, get_share_price

demo = Account(1000)

def create_account(initial_deposit):
    global demo
    demo = Account(initial_deposit)
    return "Account created with initial deposit of " + str(initial_deposit)

def deposit(amount):
    try:
        demo.deposit(float(amount))
        return "Deposit successful. New balance: " + str(demo.get_balance())
    except Exception as e:
        return str(e)

def withdraw(amount):
    try:
        demo.withdraw(float(amount))
        return "Withdrawal successful. New balance: " + str(demo.get_balance())
    except Exception as e:
        return str(e)

def buy(symbol, quantity):
    try:
        demo.buy(symbol, int(quantity))
        return "Buy successful. New holdings: " + str(demo.get_holdings())
    except Exception as e:
        return str(e)

def sell(symbol, quantity):
    try:
        demo.sell(symbol, int(quantity))
        return "Sell successful. New holdings: " + str(demo.get_holdings())
    except Exception as e:
        return str(e)

def get_holdings():
    return str(demo.get_holdings())

def get_balance():
    return str(demo.get_balance())

def get_profit_loss():
    return str(demo.get_profit_loss())

def get_transactions():
    return str(demo.get_transactions())

demo_app = gr.Blocks()

with demo_app:
    gr.Markdown("# Trading Simulation Platform")
    gr.Markdown("## Account Management")
    
    with gr.Row():
        initial_deposit = gr.Number(label="Initial Deposit")
        create_account_button = gr.Button("Create Account")
        create_account_button.click(create_account, inputs=initial_deposit, outputs="output_create_account")
        output_create_account = gr.Textbox(label="Output")
        
    with gr.Row():
        amount = gr.Number(label="Amount")
        deposit_button = gr.Button("Deposit")
        deposit_button.click(deposit, inputs=amount, outputs="output_deposit")
        output_deposit = gr.Textbox(label="Output")
        
    with gr.Row():
        amount = gr.Number(label="Amount")
        withdraw_button = gr.Button("Withdraw")
        withdraw_button.click(withdraw, inputs=amount, outputs="output_withdraw")
        output_withdraw = gr.Textbox(label="Output")
        
    gr.Markdown("## Trading")
    
    with gr.Row():
        symbol = gr.Dropdown(["AAPL", "TSLA", "GOOGL"], label="Symbol")
        quantity = gr.Number(label="Quantity")
        buy_button = gr.Button("Buy")
        buy_button.click(buy, inputs=[symbol, quantity], outputs="output_buy")
        output_buy = gr.Textbox(label="Output")
        
    with gr.Row():
        symbol = gr.Dropdown(["AAPL", "TSLA", "GOOGL"], label="Symbol")
        quantity = gr.Number(label="Quantity")
        sell_button = gr.Button("Sell")
        sell_button.click(sell, inputs=[symbol, quantity], outputs="output_sell")
        output_sell = gr.Textbox(label="Output")
        
    gr.Markdown("## Account Information")
    
    with gr.Row():
        get_holdings_button = gr.Button("Get Holdings")
        get_holdings_button.click(get_holdings, outputs="output_holdings")
        output_holdings = gr.Textbox(label="Output")
        
    with gr.Row():
        get_balance_button = gr.Button("Get Balance")
        get_balance_button.click(get_balance, outputs="output_balance")
        output_balance = gr.Textbox(label="Output")
        
    with gr.Row():
        get_profit_loss_button = gr.Button("Get Profit/Loss")
        get_profit_loss_button.click(get_profit_loss, outputs="output_profit_loss")
        output_profit_loss = gr.Textbox(label="Output")
        
    with gr.Row():
        get_transactions_button = gr.Button("Get Transactions")
        get_transactions_button.click(get_transactions, outputs="output_transactions")
        output_transactions = gr.Textbox(label="Output")

demo_app.launch()
