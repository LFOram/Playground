#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

found = False
x=0
check = [11,13,14,16,17,18,19,20]

while not found:
    x += 2520
    print(x)
    for y in check:
        if x%y == 0:
            if y == 20:
                found = True
        else:
            break
print(x)

#232792560

#yeah that could be quicker.
#must be multiple of 2520?