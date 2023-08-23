# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter



n = int(input())
a = []
list1 = []

for i in range(n):
    str = input()
    a.append(str)


list3 = set(a)

count = Counter(a)

list2 = list(count.values())

print(len(list3))

for i in range(len(list2)):
    print(list2[i], end=" ")
