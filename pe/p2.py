# p2: https://projecteuler.net/problem=2

def fibSum():
    done = False
    i_0 = 1
    i_1 = 2
    total = 2

    while (not done):
        i_3 = i_0 + i_1
        if i_3 > 4000000:
            break
        if i_3 % 2 == 0:
            total += i_3
        i_0 = i_1
        i_1 = i_3
    return total
    
if __name__ == "__main__":
    print(fibSum())

