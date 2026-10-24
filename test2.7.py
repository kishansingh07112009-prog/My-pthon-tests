session = int(input())

miuntes = int(input())

base = session ** 2

pack_bonus = (miuntes // 60) * 5

leftover_penalty = miuntes % 60

adjusted = base + pack_bonus

leftover_penalty

final_score = adjusted / 10

print(f"{final_score:.2f}")