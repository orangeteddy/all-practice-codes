def sumTo():
    """ Return the sum of reciprocals of powers of 2 """

    y  = 1
    x = 0
    while theSum != 0:
        theSum = 1/2**aNumber
        aNumber = aNumber + 1
    return aNumber

print(sumTo())

#this program calculates 1 / 2^x and determines if y will ever reach 0 if x continues increasing.
#if y ever reaches 0, the interpreter will print what the value of x is when y is 0.
#mathematically, y will never equal 0, but 1025 is printed and the loop didn't terminate
