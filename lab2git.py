def decimalToBin(n):
    result = 0
    p = 1
    while n:
        result = result + n % 2 * p
        p *= 10
        n //= 2
    return "0b" + str(result)


def bin_to_hex(number):
    if number == 0:
        return "0x0"

    hex_digits = "0123456789ABCDEF"
    hex_string = ""

    while number > 0:
        remainder = number % 16
        hex_string = hex_digits[remainder] + hex_string
        number //= 16

    return "0x" + hex_string


def lenNum(number, str):
    length = len(str)
    p = 1
    result = 0
    while number:
        result = result * 10 + number % length
        p *= 10
        number //= length
    newresult = ''
    while (result):
        newresult = newresult + str[result % 10]
        result //= 10
    return newresult


def dec_to_hex(number):
    if number == 0:
        return "0x0"

    hex_digits = "0123456789ABCDEF"
    hex_string = ""

    while number > 0:
        remainder = number % 16
        hex_string = hex_digits[remainder] + hex_string
        number //= 16

    return "0x" + hex_string


def paranthesis(str):
    contor = 0
    for i in range(0, len(str)):
        if str[i] == '(':
            contor += 1
        elif str[i] == ')':
            contor -= 1
    if contor == 0:
        return True
    else:
        return False


def ex6(str):
    result = ''
    for i in range(0, len(str)):
        if (str[i] != ' '):
            print(f"{dec_to_hex(ord(str[i]))[2:]}", end="")
        else:
            print()


def ex7(str):
    contor = 0
    for i in range(0, len(str)):
        if str[i].isupper():
            contor += 1


def ex8(x, alphabet):
    rest = 0
    word = ""
    while (x):
        rest = x % len(alphabet)
        x = x//len(alphabet)
        word = str(alphabet[rest]) + word
    return word


def ex9(str):
    for i in range(0, len(str)-1):
        if str[i-1] == " " or str[i+1] == " " or i == 0:
            print(str[i], end=" ")

    print(str[len(str)-1])


def ex10(str):
    length = len(str)
    revstr = ''
    i = length - 1

    while i >= 0:
        if str[i] == ' ':
            i -= 1
            continue

        word_end = i
        while i >= 0 and str[i] != ' ':
            i -= 1
        word_start = i + 1

        revstr += str[word_start:word_end+1]

        if i >= 0:
            revstr += ' '

    return revstr


def ex11(word):
    vowels = "aeiouAEIOU"
    countVocale = 0
    countConsoane = 0
    for i in word:
        if (i in vowels):
            countVocale += 1
        elif i is not vowels and i != " ":
            countConsoane += 1
    print(str(countConsoane) + " " + str(countVocale))


def palindrome(n):
    copie_n = n
    newn = 0
    while n:
        newn = newn * 10 + n % 10
        n //= 10
    return copie_n == newn


if __name__ == "__main__":
    # print(decimalToBin(12))
    # binary_number = 0b1100
    # print(bin_to_hex(binary_number))
    # print(lenNum(301, "abcd"))
    # print(paranthesis("6+8*(5+3/2-1+6/(3+9)-7*(5+7/3)"))
    # print(ord("A"))
    # ex9("Ana are mere si mihai pere")
    # ex11("Ana are mere si mihai pere")
    ex8("abc 012")
