# Ask the user to enter a password.
# If the password is shorter than 8 characters, print "Password is too short."
# If the password doesn’t contain at least one uppercase letter, print "Password must contain an uppercase letter.".
# If the password meets both criteria, print "Password is strong."

while True:
    a=input("Enter new password:")
    has_upper=False
    
    for char in a:
        if char.isupper():
                has_upper=True
                break
    if len(a)<8:
            print("Password is too short.")
            continue
    if not has_upper:    
            print("Password must contain an uppercase letter.")
            continue
    if len(a)>8 and has_upper:
            
            print("Password is strong.") 
            break   

