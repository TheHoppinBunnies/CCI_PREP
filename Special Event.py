def right_day(total_people, schedule):
    day_count = [0] * 5

    for person in schedule:
        for i in range(5):
            if person[i] == "Y":
                day_count[i] += 1

    max_day = max(day_count)
    best_day = [str(i+1) for i in range(5) if day_count[i] == max_day]

    return ",".join(best_day)


people_attending = int(input())
schedule_per_people = [str(input()) for _ in range(people_attending)]
print(right_day(people_attending, schedule_per_people))
