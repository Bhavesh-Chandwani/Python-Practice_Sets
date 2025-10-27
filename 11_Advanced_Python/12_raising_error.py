def check_age(age):
    if age < 18:
        raise ValueError("Age must be greater than 18")
    return f"Access Granted"
try:
    print(check_age(20))
    print(check_age(17))

except ValueError as e:
    print(f"Error: {e}")