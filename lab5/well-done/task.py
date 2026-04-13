class safe_execute:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        try:
            return self.func(*args, **kwargs)
        except Exception as e:
            return f"Error: {e}"

class range_validator:
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val
    
    def validate(self, value):
        return self.min_val <= value <= self.max_val

@safe_execute
def check_values(min_val, max_val, values):
    validator = range_validator(min_val, max_val)
    return [validator.validate(v) for v in values]

print("Проверка диапазона [0, 100]:")
print(check_values(0, 100, [50, 75, 150, -10]))

print("\nПроверка диапазона [0, 10]:")
print(check_values(0, 10, [5, 8, 12, 3]))

print("\nДеление с ошибкой:")

@safe_execute
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(10, 0))