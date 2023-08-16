# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

list1 = list(map(int,input("").strip().split()))
list2 = list(map(int,input("").strip().split()))
 
#list3 = list(product(list1,list2))

A = [list1,list2]

b = list(product(*A))

for i in b:
    print(i,end=" ")
