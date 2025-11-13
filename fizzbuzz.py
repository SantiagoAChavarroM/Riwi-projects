import time
for variable in range(1, 101):

    if (variable % 5 == 0) and (variable % 3 == 0):
        print("FizzBuzz")
        time.sleep(.2)
    elif variable % 3 == 0:
        print("Fizz")
        time.sleep(.2)
    elif variable % 5 == 0:
        print("Buzz")
        time.sleep(.2)
    else:
        print(variable)
        time.sleep(.2)
