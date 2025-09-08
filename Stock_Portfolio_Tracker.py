#Task 2
stock_prices = {"AAPL":180,"TSLA":250,"GOOG":120,"AMZN":140,"MSFT":200}
total_investment = 0

print("Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock=="DONE":
        break
    if stock in stock_prices:
        qty=int(input(f"Enter quantity of {stock}: "))
        cost=stock_prices[stock]*qty
        total_investment+=cost
        print(f"Added {qty} {stock} = ${cost}")
    else:
        print("Stock not available.")

print("\nTotal Investment Value = $",total_investment)

save = input("Do you want to save result to file? (y/n): ").lower()
if save=="y":
    with open("portfolio.txt", "w") as f:
        f.write(f"Total Investment Value = ${total_investment}\n")
    print("Saved to portfolio.txt")
