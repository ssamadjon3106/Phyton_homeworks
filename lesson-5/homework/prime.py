def prime(n):
    if n<0 and n==0:
        print('Enter a positive ')
    for number in range(2, n):
        if  n%number==0:
            return False
        else:
            return True   

a=int(input("Enter a number: "))
print(prime(a))