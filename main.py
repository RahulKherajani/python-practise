def checkleapyear(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("Leap Year")
        return
    print("Not a Leap Year")


def checklargest(numlist):
    maxnum = -10000
    secondmax = -10000
    for num in numlist:
        if num > maxnum:
            secondmax = maxnum
            maxnum = num
        if secondmax < num < maxnum:
            secondmax = num
    print(maxnum, secondmax)


def reversenumber(num):
    new = 0
    while num != 0:
        new = new * 10 + num % 10
        num = num // 10
    print(new)


def isprime(num):
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True


def rangeprime(start, end):
    for num in range(start, end + 1):
        if isprime(num):
            print(num)


def isarmstrongnumber(num):
    sumofpowers = 0
    temp = num
    length = len(str(num))
    while temp != 0:
        sumofpowers += (temp % 10) ** length
        temp = temp // 10
    if sumofpowers == num:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")


def calculatehcf(num1, num2):
    hcf = 1
    if num1 < num2:
        smallest = num1
    else:
        smallest = num2
    for i in range(1, smallest + 1):
        if (num1 % i == 0) and (num2 % i == 0):
            hcf = i
    print(hcf)


def containsDuplicate(nums) -> bool:
    uniqueNums = set()
    for num in nums:
        if num in uniqueNums:
            return True
        else:
            uniqueNums.add(num)
    return False


def validAnagram(word1, word2):
    chars = set(list(word1))
    for char in chars:
        if word1.count(char) != word2.count(char):
            return False
    return True


def twoSum(nums, target):
    """ Leet Code 1 """
    prev = {}
    for i, num in enumerate(nums):
        n = target - num
        if n in prev:
            return [prev[n], i]
        prev[num] = i


def isPalindrome(sentence):
    """LeetCode 125"""
    sentence = ''.join([char.lower() for char in sentence if char.isalnum()])
    start = 0
    end = len(sentence) - 1
    while start < end:
        if sentence[start] != sentence[end]:
            return False
        start += 1
        end -= 1
    return True


def isValidParenthesis(string):
    """Leetcode 20"""
    ref = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in string:
        if char in ref:
            if stack and stack[-1] == ref[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return True if not stack else False


def main():
    print(isValidParenthesis("()[]{[]}{"))


if __name__ == "__main__":
    main()
