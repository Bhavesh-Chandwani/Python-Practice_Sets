class InvalidAgeError(Exception):
    """Custom Exceptions for Invalid Age"""
    def __init__(self, message = "Age must be greater than 18"):
        self.message = message
        super().__init__(self.message)
def verify_age(age):
    if age < 18:
        raise InvalidAgeError()
    return "Access Granted"
try:
    print(verify_age(24))
    print(verify_age(16))
except InvalidAgeError as e:
    print(f"Error : {e}")