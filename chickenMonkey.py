


def num():
    zero_hundred = range(1, 100)
    for num in zero_hundred:
        if (num) % 5 == 0 and num % 7 == 0:
            print("ChickMonkey")
        elif (num) % 5 == 0:
            print("Chicken")
        elif (num) % 7 == 0:
            print("Monkey")
        else:
            print(num)


num()