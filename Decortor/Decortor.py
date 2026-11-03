def my_decorstor(func):

    def wrapper():
        print("Function Started")
        func()
        print("function ended")
    return wrapper

def greet():
    print("Hello")


greet = my_decorstor(greet)
greet()