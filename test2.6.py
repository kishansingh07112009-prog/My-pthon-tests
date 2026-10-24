qty_str = input()

price_str = input()

print(type(qty_str))

qty = int(qty_str)

print(type(qty))

price = float(price_str)

total = qty * price


print(f"{total:.2f}")