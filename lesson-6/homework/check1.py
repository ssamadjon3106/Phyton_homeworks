def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        return func(a, b)
    return wrapper

@check
def div(a, b):
    return a / b

s1 = div(6, 3)
s2 = div(10, 0)

print(s1)  # Should print: 2.0
print(s2)  # Should print: Error: Division by zero is not allowed.
