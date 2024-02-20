def points(pkg, obs):
    score = 0

    if pkg > obs:
        score = 500 + (50 * pkg) - (10 * obs)

    else:
        score = (50*pkg) - (10*obs)

    return score


pkg = int(input())
obs = int(input())

print(points(pkg, obs))
