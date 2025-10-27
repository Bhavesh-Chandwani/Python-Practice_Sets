def upper_case(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

def exclaimed(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + "!!!"
    return wrapper

@upper_case
@exclaimed
def greet(name):
    return(f"Hello {name}!")
print(greet("John"))