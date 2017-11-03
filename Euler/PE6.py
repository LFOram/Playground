#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
def sumsquare(nums):
    total = 0
    for i in nums:
        total += i**2
    return total

def squaresum(nums):
    return (sum(nums)**2)

numbers = list(range(101))
print(squaresum(numbers)-sumsquare(numbers))