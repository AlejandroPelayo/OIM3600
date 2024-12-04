from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
import yfinance as yf

app = FastAPI()

templates = Jinja2Templates(directory="templates")

portfolio = {}
cash_balance = 100000  # starting with $100,000

@app.get('/')
async def index(request: Request):
    # Fetch real-time prices for each stock in the portfolio
    real_time_prices = {}
    total_value = cash_balance  # Start with the cash balance
    
    for symbol, data in portfolio.items():
        stock = yf.Ticker(symbol)
        stock_price = stock.history(period="1d")['Close'][0]
        real_time_prices[symbol] = round(stock_price, 2)
        total_value += stock_price * data['quantity']  # Add value of stocks to total value
    
    # Clean portfolio to only show quantities
    clean_portfolio = {symbol: data['quantity'] for symbol, data in portfolio.items()}
    
    return templates.TemplateResponse(
        "index.html", 
        {
            "request": request,
            "portfolio": clean_portfolio,
            "real_time_prices": real_time_prices,  # Add real-time prices to the template context
            "cash_balance": cash_balance,
            "total_value": round(total_value, 2)  # Add total value to the context
        }
    )

@app.post("/buy")
async def buy(request: Request, symbol: str = Form(...), quantity: int = Form(...)):
    global cash_balance

    symbol = symbol.upper()  # Ensure symbol is uppercase

    stock = yf.Ticker(symbol)
    stock_price = stock.history(period="1d")['Close'][0]

    total_cost = stock_price * quantity 

    if total_cost > cash_balance:
        return templates.TemplateResponse('index.html', {"request": request, "error": "Error - Not enough cash to complete purchase", "portfolio": portfolio, "cash_balance": cash_balance})

    cash_balance -= total_cost

    if symbol in portfolio:
        portfolio[symbol]['quantity'] += quantity
        portfolio[symbol]['avg_price'] = ((portfolio[symbol]['avg_price'] * portfolio[symbol]['quantity']) + (stock_price * quantity)) / (portfolio[symbol]['quantity'] + quantity)
    else:
        portfolio[symbol] = {'quantity': quantity, 'avg_price': stock_price}

    # Fetch real-time prices for each stock in the portfolio
    real_time_prices = {}
    for symbol in portfolio:
        stock = yf.Ticker(symbol)
        stock_price = stock.history(period="1d")['Close'][0]
        real_time_prices[symbol] = round(stock_price, 2)

    return templates.TemplateResponse('index.html', {
        "request": request,
        "portfolio": portfolio,
        "cash_balance": cash_balance,
        "real_time_prices": real_time_prices,  # Pass real-time prices to the template
    })

@app.post("/sell")
async def sell(request: Request, symbol: str = Form(...), quantity: int = Form(...)):
    global cash_balance
    symbol = symbol.upper()  # Ensure symbol is uppercase

    # Check if the symbol exists in the portfolio and if the quantity is available
    if symbol not in portfolio:
        return templates.TemplateResponse("index.html", {"request": request, "error": f"Error - {symbol} not found in portfolio", "portfolio": portfolio, "cash_balance": cash_balance})

    if portfolio[symbol]['quantity'] < quantity:
        return templates.TemplateResponse("index.html", {"request": request, "error": f"Error - Not enough shares of {symbol} to sell", "portfolio": portfolio, "cash_balance": cash_balance})

    # Fetch the real-time price of the stock
    stock = yf.Ticker(symbol)
    stock_price = stock.history(period="1d")['Close'][0]

    total_revenue = stock_price * quantity
    cash_balance += total_revenue

    # Update the portfolio
    portfolio[symbol]['quantity'] -= quantity
    if portfolio[symbol]['quantity'] == 0:
        del portfolio[symbol]  # Remove the stock from the portfolio if no quantity remains

    # Fetch real-time prices for each stock in the portfolio
    real_time_prices = {}
    total_value = cash_balance  # Start with the cash balance
    
    for symbol, data in portfolio.items():
        stock = yf.Ticker(symbol)
        stock_price = stock.history(period="1d")['Close'][0]
        real_time_prices[symbol] = round(stock_price, 2)
        total_value += stock_price * data['quantity']  # Add value of stocks to total value

    return templates.TemplateResponse('index.html', {
        "request": request,
        "portfolio": portfolio,
        "cash_balance": cash_balance,
        "real_time_prices": real_time_prices,  # Pass real-time prices to the template
        "total_value": round(total_value, 2)  # Pass total value to the template
    })

# Test route
@app.get('/test')
async def test():
    return {"message": "Hello, FastAPI is working!"}
