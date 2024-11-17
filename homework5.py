from utils import process_item

if __name__ == "__main__":
    while True:
        user_input = input("Enter a number (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        try:
            number = int(user_input)
            print(process_item(number))
        except ValueError:
            print("Please enter a valid number.")



def my_function(*args, **kwargs):
    return sum(kwargs.values())

anonymous_function = lambda *args, **kwargs: sum(kwargs.values())

print(my_function(1, 2, c=3, d=4))
print(anonymous_function(1, 2, c=3, d=4))


def extract_vowels(s):
    return [char for char in s if char.lower() in 'aeiou']


extract_vowels_lambda = lambda s: list(filter(lambda char: char.lower() in 'aeiou', s))

extract_vowels_listcomp = lambda s: [char for char in s if char.lower() in 'aeiou']



def filter_dictionaries(*args, **kwargs):
    return [
        d for d in args if isinstance(d, dict) and len(d) >= 2 and 
        any(isinstance(k, str) and len(k) >= 3 for k in d)
    ]

print(filter_dictionaries(
    {1: 2, 3: 4, 5: 6},
    {'a': 5, 'b': 7, 'c': 'e'},
    {2: 3},
    [1, 2, 3],
    {'abc': 4, 'def': 5},
    3764,
    dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
    test={1: 1, 'test': True}
))

def extract_numbers(lst):
    return [item for item in lst if isinstance(item, (int, float))]


print(extract_numbers([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0])) 

def process(**kwargs):
    fib = [0, 1]
    for _ in range(998):
        fib.append(fib[-1] + fib[-2])

    if "filters" in kwargs:
        for predicate in kwargs["filters"]:
            fib = list(filter(predicate, fib))

    if "offset" in kwargs:
        fib = fib[kwargs["offset"]:]

    if "limit" in kwargs:
        fib = fib[:kwargs["limit"]]

    return fib


def sum_digits(x):
    return sum(map(int, str(x)))

print(process(
    filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
    limit=2,
    offset=2
)) 



def print_arguments(function):
    def wrapper(*args, **kwargs):
        print(f"Arguments are: {args}, {kwargs}")
        return function(*args, **kwargs)
    return wrapper


def multiply_output(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs) * 2
    return wrapper


def augment_function(function, decorators):
    for decorator in decorators:
        function = decorator(function)
    return function


def add_numbers(a, b):
    return a + b

decorated_function = augment_function(add_numbers, [print_arguments, multiply_output])
print(decorated_function(3, 4)) 

def process_pairs(pairs):
    return [
        {
            "sum": x + y,
            "prod": x * y,
            "pow": x ** y
        }
        for x, y in pairs
    ]

print(process_pairs([(5, 2), (19, 1), (30, 6), (2, 2)]))