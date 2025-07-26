for numero in range(1, 101):
    if numero % 5 == 0:
        if numero % 7 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif numero % 7 == 0:
        print("Buzz")