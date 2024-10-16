from collections import Counter
from numpy import sqrt, ceil


def firstFibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib


def isPrime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int((sqrt(n)))+1):
        if n % i == 0:
            return False
    return True


def primeNumbers(n):
    primes = []
    for number in n:
        if isPrime(number):
            primes.append(number)
    return primes


def logicalOperations(a, b):
    intersected = []
    reunited = []
    aminusb = []
    bminusa = []
    for number in a:
        if number in b:
            intersected.append(number)

    for number in a:
        reunited.append(number)

    for number in b:
        if number not in reunited:
            reunited.append(number)
    reunited.sort()

    for number in a:
        if number not in b:
            aminusb.append(number)

    for number in b:
        if number not in a:
            bminusa.append(number)
    return intersected, reunited, aminusb, bminusa


def compose(notes, moves, start_pos):
    song = []
    current_pos = start_pos

    song.append(notes[current_pos])

    for move in moves:
        current_pos = (current_pos + move) % len(notes)
        song.append(notes[current_pos])
    return song


def matrixUnderDiag(n):
    length = len(n)
    for i in range(0, length):
        for j in range(0, length):
            if i > j:
                n[i][j] = 0
    return n


def manyArgs(x, *args):
    combined_list = []
    for sublist in args:
        for item in sublist:
            combined_list.append(item)

    counts = Counter(combined_list)
    result = []
    for item, count in counts.items():
        if count == x:
            result.append(item)
    return result


def isPalindrome(n):
    res = str(n) == str(n)[::-1]
    return res


def howManyPals(n):
    maxSize = -1
    howMany = 0
    for number in n:
        if isPalindrome(number):
            howMany += 1
            if len(str(number)) > maxSize:
                maxSize = len(str(number))
    return (howMany, maxSize)


def ex8(x=1, n=None, flag=True):
    result = []
    for strn in n:
        smallResult = []
        for i in strn:
            if flag == True:
                if ord(i) % x == 0:
                    smallResult.append(i)
            else:
                if ord(i) % x != 0:
                    smallResult.append(i)
        if len(smallResult) > 0:
            result.append(smallResult)
    return result


def ex9(n):
    result = []
    rows = len(n)
    cols = len(n[0])

    for i in range(rows):
        for j in range(cols):
            current_height = n[i][j]
            for front_row in range(i):
                if n[front_row][j] > current_height:
                    result.append((i, j))
                    break

    return result


def ex10(args):
    maxim = -1
    for arg in args:
        if (len(arg) > maxim):
            maxim = len(arg)
    result = []
    for i in range(maxim):
        smalResult = []
        for arg in args:
            if (i < len(arg)):
                smalResult.append(arg[i])
            else:
                smalResult.append(None)
        result.append(tuple(smalResult))
    return result


def getTup(tuples):
    return tuples[1][2]


def ex11(tuples):
    result = []
    for tup in tuples:
        result.append(tup)
    result.sort(key=getTup)
    return result


def ex12(n):
    result = {}

    for word in n:
        rima = word[-2:]
        if rima not in result:
            result[rima] = []
        result[rima].append(word)

    return list(result.values())


# Example usage
result = group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte'])
print(result)


if __name__ == "__main__":
    # print(firstFibonacci(15))
    # print()
    # print(logicalOperations([15, 20, 27, 30], [15, 27, 85, 101]))
    # print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
    # print(matrixUnderDiag([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # print(manyArgs(1, 2, 3, 4))
    # print(howManyPals([123, 121, 1111112111111]))
    # print(ex8(2, ["test", "hello", "lab002"], False))

    print(ex11([('abc', 'bcd'), ('abc', 'zza')]))
