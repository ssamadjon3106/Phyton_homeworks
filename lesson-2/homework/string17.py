a=input("enter a string: ")
vowels=['a', 'e', 'o', 'u', 'i', 'o' ]
for v in vowels:
    a= a.replace(v, '*')
print(a)