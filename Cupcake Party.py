def total_cupcakes(R, S):
    if ((R * 8) + (S * 3)) > 28:
        return ((R * 8) + (S * 3)) - 28

    else:
        return 0


R = int(input())
S = int(input())

print(total_cupcakes(R, S))