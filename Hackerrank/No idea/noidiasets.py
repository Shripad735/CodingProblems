# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    happiness = 0
    n, m = map(int, input().strip().split(' '))
    list = list(map(int, input().strip().split(' ')))
    
    seta = set(map(int, input().strip().split(' ')))
    setb = set(map(int, input().strip().split(' ')))

    for i in list:
        if i in seta:
            happiness += 1
        elif i in setb:
            happiness -= 1
        else:
            pass
    print(happiness)
