

def get(number):
    is_fizz, is_buzz = number % 3 == 0, number % 5 == 0
    if is_fizz and is_buzz:
        return "fizzbuzz"
    elif is_fizz:
        return "fizz"
    elif is_buzz:
        return "buzz"
    else:
        return number

