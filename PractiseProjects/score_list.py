scores = []

score = int(input("Score: "))
while score >= 0:
    scores.append(score)
    score = int(input("Score: "))
if score > 0:
    print("You highest score is", max(scores))
else:
    print("Error")