text = "sadasdre2324"
c = 0
for i in text:
    if i.isdigit():
        print("String contains digit")
        break
    else:
        c += 1
if c == len(text):
    print("String does not contain any digit")


# if any(text.isdigit() for char in text):
#     print('it contains the number')
# else:
#     print('ts does not contain the number')