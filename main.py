def checkleapyear(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("Leap Year")
        return
    print ("Not a Leap Year")


def checklargest(numlist):
    max = -10000
    secondmax = -10000
    for num in numlist:
        if num > max:
            secondmax = max
            max = num
        if secondmax < num < max:
            secondmax = num
    print(max, secondmax)

def reversenumber(num):
    new = 0;
    while (num!= 0):
        new = new * 10 + num % 10
        num = num // 10
    print(new)

def isprime(num):
    for i in range(2, num//2):
        if num % i == 0:
            print("Not Prime")
            return
    print("Prime")

def main():
    isprime(27)


if __name__ == "__main__":
    main()