def convert_cel_to_far(c):
    f = c * 9 / 5 + 32
    return round(f, 2)

def convert_far_to_cel(f):
    c = (f - 32) * 5 / 9
    return round(c, 2)


f = float(input('Enter a temperature in degrees F: '))
celsius = convert_far_to_cel(f)
print(f'{f} degrees F = {celsius} degrees C')

c = float(input('Enter a temperature in degrees C: '))
fahrenheit = convert_cel_to_far(c)
print(f'{c} degrees C = {fahrenheit} degrees F')


