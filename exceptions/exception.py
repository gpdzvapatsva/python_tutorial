def division(x,y):
    try:
        answer=x/y
        print ("The answer is ", answer)
    except ZeroDivisionError:
        print("Can not divide by 0")
    except TypeError:
        print("can not use strings")
    finally:
        print("We are done")
number1=int(input("enter number"))
number2=int(input("enter number"))
division(number1,number2)
