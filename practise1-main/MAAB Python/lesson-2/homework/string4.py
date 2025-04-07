
text = input("Enter a string: ")

text = text.replace(" ", "").lower()


if text == text[::-1]:
    print("The string is a palindrome!")
else:
    print("The string is not a palindrome.")

