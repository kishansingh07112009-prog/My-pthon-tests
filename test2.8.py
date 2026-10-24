percentage = float(input())

extracurricular_score = float(input())


attendance = float(input())


qualified = (percentage >= 85) or (extracurricular_score >= 90 and attendance >= 75)

print(qualified)