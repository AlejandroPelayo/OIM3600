def calculate_cost():
    """
    Get data from a file, print the table and total cost
    """
    total = 0
    stocks = []

    with open("data/portfolio.csv", "r") as file:
        for i, line in enumerate(file):
            # print(line)
            # if it is the first line: skip it
            # split each line to get name, share and price
            # calculate the total cost of each stock
            # add it to total
            # print the stock line in a nice way
            if i == 0:
                print("name     share     price")
                continue
            stock = line.strip('\n').split(",") # stock is a list
            stocks.append(stock)
            # print(stock)
            name, share, price = stock # unpacking
            # name = stock[0]
            share = int(share)
            price = float(price)
            print(f"{name:5}{share:100}{price:10.2f}")
            cost = share * price
            total += cost 
    print(f"Total Cost: ${total:.2f}")
    return stocks

stocks = calculate_cost()

# today I am buying more shares (100 shares each), calculate the total cost
# 1. What data structure to store the original data? dict 
# 2. How to update 
print(stocks)

# is it easy to update shres of each stock in a list?
for stock in stocks: # stocks is a list, stock is also a list
    stock[1] = int(stock[1]) + 100