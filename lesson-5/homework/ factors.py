def factors(n):
    for number in range (1, n+1):
        if n%number==0:
            print(f'{number} is factor of {n}')
s=int(input('Enter a positive integer: '))            
factors(s)
