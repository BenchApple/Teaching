## Ben Chappell

def main():
    sum = 0
    
    for i in range(0, 1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    print (sum)


def withWhile():
    sum = 0

    limit = 1000
    i = 0
    while (i < limit):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
        i += 1

    print (sum)

def withAdvanced():
    s = sum([i for i in range(0, 1000) if i % 3 == 0 or i % 5 == 0])
    print (s)

if __name__ == "__main__":
    main()
    withWhile()
    withAdvanced()