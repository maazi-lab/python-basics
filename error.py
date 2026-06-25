class InvalidAgeError(Exception):
    pass

age = 150

if age > 100:
    raise InvalidAgeError("Invalid age")
