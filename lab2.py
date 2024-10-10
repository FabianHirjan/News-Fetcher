import sys


def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def cmmdc():
    arguments = list(map(int, sys.argv[1:]))

    gcd = find_gcd(arguments[1], arguments[2])

    for i in range(3, len(arguments)):
        gcd = find_gcd(gcd, arguments[i])

    return gcd


def findVowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for i in word:
        if (i in vowels):
            count += 1
    return count


def occurences(str1, str2):
    count = str2.count(str1)
    return count


def camel(str):
    result = str[0].lower()
    for i in str[1:]:
        if i.isupper():
            result += "_"
        result += i
    return result.lower()


def palindrome(n):
    copie_n = n
    newn = 0
    while n:
        newn = newn * 10 + n % 10
        n //= 10
    return copie_n == newn


def findNumber(text):
    result = ""
    i = 0
    while i < len(text):
        if text[i].isdigit():
            while i < len(text) and text[i].isdigit():
                result += text[i]
                i += 1
            return result
        i += 1
    return result


def binary(n):
    str = bin(n)
    return str.count("1")


def words(str):
    count = str.count(" ")
    if count == 0:
        return count
    else:
        return count + 1


def words(str):
    count = 1
    for i in range(0, len(str)):
        if str[i] == ' ' and str[i-1] != ' ' and str[i+1] != ' ':
            count += 1
    return count


if __name__ == "__main__":
    print(words("I have python exam"))
