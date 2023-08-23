n = int(input())
s = set(map(int, input().split()))
n1 = int(input())

for i in range(n1):
    try:
        inp = input().split()
        if inp[0] == "pop":
            s.pop()
        elif inp[0] == "remove":
            s.remove(int(inp[1]))
        elif inp[0] == "discard":
            s.discard(int(inp[1]))
    except KeyError:
        pass
    
sum1 = sum(s)

print(sum1)
    
