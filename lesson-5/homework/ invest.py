def invest(amount, years):
    for year in range(1, years+1):
        amount*=(1+ .05)
        print(f'Year {year}: $ {round(amount, 2)}')
print(invest(100, 4))
       
       
