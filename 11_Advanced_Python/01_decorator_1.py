def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"This function is about to execute.")
        func(*args, **kwargs)
        print(f"This function is executed.")
    return wrapper

@decorator
def say_hello(name):
    print(f"Hello {name}!")
say_hello("John")