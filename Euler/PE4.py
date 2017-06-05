#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

maxi = 0
for x in range(100,1000):
    for y in range(100,1000):
        forw = x*y
        back = str(forw)[::-1]
        if str(forw) == back and forw > maxi:
            maxi = forw

print(maxi)