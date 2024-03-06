# this file is to transfor a number to ieee format


from math import log2, floor


# example: convert 50 to  1.10010 × 2^5 (a form of m*2^n)

n = floor( log2(50) )  # n = log2(50/m) Since m is in range 1 to 2 and n is integer, n is floor of log2(50)
m = 50 / ( 2**n )
print(m*2**n)  # 50
print(n, m)


# todo: convert 2^x to ieee format


# todo: convert cos(x) to ieee format


# todo: convert exp(x) to ieee format


# todo: convert log2(x) to ieee format