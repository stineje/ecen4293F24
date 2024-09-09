def payment(P, APR, yrs):
    """
    determine the monthly payment for a loan
    input:
        P:    principal, or amount borrowed
        APR:  annual percentage rate
        yrs:  term of the loan in years
    output: 
        pmt:  monthly payment
    """
    n = yrs*12
    i = APR/100/12
    pmt = P * i*(1+i)**n/((1+i)**n-1)
    return pmt


LoanAmt = 40000
APR = 5.3
print('Term    Monthly\n(yrs)   Payment')
for n in range(3, 7):
    pmt = payment(LoanAmt, APR, n)
    print('{0:3d}    {1:8,.2f}'.format(n, pmt))
