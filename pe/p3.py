# p3: https://projecteuler.net/problem=3


def findAFactor(i):
    done = False
    i_1 = 1
    i_2 = 2

    while not done:
        if i %  i_2 != 0:
            past = i_2
            i_2 = i_1 + i_2
            i_1 = past
        else: 
            print(i / i_2)
            if i / i_2 == i_2:
                return i_2
            i = i / i_2
            past = i_2
            i_2 = i_1 + i_2
            i_1 = past
    

if __name__ == "__main__":
    findAFactor(13195)