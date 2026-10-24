occupied = int(input())

total = int(input())

wifi_flag = int(input())

empty = total - occupied

print("#" * occupied + "-" * empty)

print(bool(wifi_flag))