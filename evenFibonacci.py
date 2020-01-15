## Ben Chappell

def main():
    limit = 4000000
    s = 2

    prevTwoValues = [2,1]
    nextFibVal = sum(prevTwoValues)

    while(nextFibVal <= limit):
        if nextFibVal % 2 == 0:
            s += nextFibVal

        prevTwoValues[1] = prevTwoValues[0]
        prevTwoValues[0] = nextFibVal
        nextFibVal = sum(prevTwoValues)

    print(s)


if __name__ == "__main__":
    main()