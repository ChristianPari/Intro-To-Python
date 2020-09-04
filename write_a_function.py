# python functions are defined with the def keyword
def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    
    return leap

year = int(raw_input())
print is_leap(year)

# functions (by default) have to be called with the correct amount of arguments
# if unsure how many arguments you will be using use *args as the parameter, can access arguments via indexes
# can pass key/value as arguements
# def func(ex1, ex2)
# func(ex1 = True, ex2 = False)
# if unsure how many keyword arguments you'll need use **kwargs to be able to pass in as many key/value args and then access them within the function via bracket notation