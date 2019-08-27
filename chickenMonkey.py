


def num():
    zero_hundred = range(0, 100)
    for num in zero_hundred:
        if (num+1) % 5 == 0 and num % 7 == 0:
            print("ChickMonkey")
        elif (num+1) % 5 == 0:
            print("Chicken")
        elif (num+1) % 7 == 0:
            print("Monkey")
        else:
            print(num+1)


num()