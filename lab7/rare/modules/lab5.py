from functools import wraps

def create_range_validator(min_val, max_val):
    def validator(value):
        return min_val <= value <= max_val
    return validator

def safe_execute(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"Error: {e}"
    return wrapper

@safe_execute
def check_values(min_val, max_val, values):
    validator = create_range_validator(min_val, max_val)
    return [validator(v) for v in values]

@safe_execute
def divide(a, b):
    return a / b

def run():
    print("Lab5: check_values(0, 100, [50, 150, -5]) =", check_values(0, 100, [50, 150, -5]))
    print("Lab5: divide(10, 2) =", divide(10, 2))
    print("Lab5: divide(10, 0) =", divide(10, 0))