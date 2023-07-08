def happy_new_year():
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
    print("Happy New Year!")

def fizzbuzz_printer():
    for num in range(1, 101):
        print(fizzbuzz(num))

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


def reverse_string(string):
    reversed_str = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_str += string[i]
    return reversed_str

def square_integers(int_list):
    return [num ** 2 for num in int_list]
