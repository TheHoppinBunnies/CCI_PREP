def rating(p, f):
    return (p * 5) - (f * 3)


N = int(input())

score = 0
star = False

for i in range(N):
    points = int(input())
    fouls = int(input())

    if rating(points, fouls) > 40:
        score += 1

if score == N:
    star = True

if star:
    print(f"{score}+")

else:
    print(score)
