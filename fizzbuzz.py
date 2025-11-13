for variable in range(1, 101):

    if (variable % 5 == 0) and (variable % 3 == 0):
        print("FizzBuzz")
    elif variable % 3 == 0:
        print("Fizz")
    elif variable % 5 == 0:
        print("Buzz")
    else:
        print(variable)
    
    