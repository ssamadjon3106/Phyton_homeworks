a = input('enter a organization name: ')
first= ''
for word in a.split():
    first+= word[0]
first= first.upper()
print(first)