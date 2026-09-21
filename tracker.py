# PNG Trade Store Stock Tracker - by Buckley Sumani
# Helps small shops in Moresby track sales and profit

print("=== TRADE STORE TRACKER - PNG ===")
store_name = input("Enter store name: ")

products = []
total_profit = 0

for i in range(3):
    print(f"\n--- Product {i+1} ---")
    name = input("Product name (e.g., rice, tinned fish): ")
    buy_price = float(input(f"How much you buy {name} for (Kina): "))
    sell_price = float(input(f"How much you sell {name} for (Kina): "))
    quantity = int(input(f"How many {name} in stock: "))

    profit_per_item = sell_price - buy_price
    total_value = sell_price * quantity
    profit = profit_per_item * quantity
    total_profit += profit

    products.append([name, quantity, total_value, profit])
    print(f"Profit for {name}: K{profit}")

# Final Report
print("\n=================================")
print(f"STORE REPORT: {store_name}")
print("=================================")
for p in products:
    print(f"{p[0]} - Stock: {p[1]} - Value: K{p[2]} - Profit: K{p[3]}")

print("---------------------------------")
print(f"TOTAL EXPECTED PROFIT: K{total_profit}")
print("---------------------------------")

# Save to file like real Data Factory pipeline
with open("store_report.txt", "w") as f:
    f.write(f"Store: {store_name}\n")
    for p in products:
        f.write(f"{p[0]}, Qty: {p[1]}, Value: K{p[2]}, Profit: K{p[3]}\n")
    f.write(f"TOTAL PROFIT: K{total_profit}\n")

print("\nReport saved to store_report.txt")
print("You can show this file to shop owner!")
