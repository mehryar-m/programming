# Problem: https://projecteuler.net/problem=1
# Sum of multiples of 3 & 5 up to 1000

def findSum(low, high):
    total = 0 
    for i in range(low, high):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


if __name__ == "__main__":
    print(findSum(0,1000))