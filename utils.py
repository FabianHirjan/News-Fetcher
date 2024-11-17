def process_item(x):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    x += 1
    while not is_prime(x):
        x += 1
    return x

if __name__ == "__main__":
    user_input = int(input("Enter a number: "))
    print(process_item(user_input))
