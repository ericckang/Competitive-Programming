#
# Complete the 'getNetProfit' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts STRING_ARRAY events as parameter.
#

def getNetProfit(events):
    net_profit_losses = [] # Store profit and losses to each query event

    stock_data = {}  # A dictionary to store data for each stock

    for event in events:
        action, *params = event.split()

        if action == 'BUY':
            stock, quantity = params[0], int(params[1])
            if stock not in stock_data:
                stock_data[stock] = {'quantity': 0, 'total_spent': 0, 'stock_price': 0}
            stock_data[stock]['total_spent'] += quantity * stock_data[stock]['stock_price']
            stock_data[stock]['quantity'] += quantity

        elif action == 'SELL':
            stock, quantity = params[0], int(params[1])
            stock_data[stock]['total_spent'] -= quantity * stock_data[stock]['stock_price']
            stock_data[stock]['quantity'] -= quantity

        elif action == 'CHANGE':
            stock, price_change = params[0], float(params[1])
            if stock not in stock_data:
                stock_data[stock] = {'quantity': 0, 'total_spent': 0, 'stock_price': 0}
            stock_data[stock]['stock_price'] += price_change

        elif action == 'QUERY':
            net_profit_loss = sum(
                (data['quantity'] * data['stock_price'] - data['total_spent'])
                for data in stock_data.values()
            )
            net_profit_losses.append(round(net_profit_loss))

    return net_profit_losses
