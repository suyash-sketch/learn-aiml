from functools import wraps

def my_decorator(func):

    @wraps(func)
    def wrapper():
        num = 4
        print("Before function runs")
        func(num)
        print("After function runs")
    return wrapper

@my_decorator
def greet(num):
    print("Hello from decorators class from chaicode", num)


greet()

print(greet.__name__)