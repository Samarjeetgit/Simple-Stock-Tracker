# Simple Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 300
}

portfolio = {}

print("Enter your stock details (type 'done' to finish)\n")

while True:
    stock = input("Enter stock name: ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available. Try again.\n")
        continue

    try:
        qty = int(input("Enter quantity: "))
    except:
        print("Invalid quantity\n")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + qty

# Calculate total investment
total = 0

print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total += value
    print(f"{stock} - {qty} shares → ${value}")

print(f"\nTotal Investment Value: ${total}")

# Save to file
with open("portfolio.txt", "w") as f:
    f.write(f"Total Investment: ${total}\n")

print("\nSaved to portfolio.txt")