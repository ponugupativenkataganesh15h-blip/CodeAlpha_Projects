stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 300
}

total = 0
portfolio = {}

n = int(input("How many stocks do you want to enter? "))

for i in range(n):
    name = input("Enter stock name: ").upper()
    qty = int(input("Enter quantity: "))

    if name in stocks:
        value = stocks[name] * qty
        total += value
        portfolio[name] = value
    else:
        print("Stock not found!")

print("\nPortfolio Value:")
for stock, value in portfolio.items():
    print(stock, ":", value)

print("Total Investment:", total)

# Save to file
with open("portfolio.txt", "w") as f:
    for stock, value in portfolio.items():
        f.write(f"{stock}: {value}\n")
    f.write(f"Total: {total}")
