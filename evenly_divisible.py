# Create a function that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided by c from the range a, b inclusive.

def evenly_divisible(a, b, c) :
    summ = 0
    mini = min(a,b)
    maxi = max(a,b)
    if c <= maxi :
        for i in range(mini, maxi+1) :
            if i % c == 0 :
                summ += i
        return summ
    else :
        return 0

print(evenly_divisible(1, 10, 20))
print(evenly_divisible(10, 1, 2))
print(evenly_divisible(1, 10, 3))