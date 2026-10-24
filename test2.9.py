opening = float(input())

topup = float(input())

spend = float(input())

cashback_fee = float(input())

platform_fee = float(input())

refund = float(input())

balance = opening + topup

balance = balance - spend

balance = balance * cashback_fee

balance = balance -  platform_fee

balance = balance + refund

print(f"{balance:.2f}")