# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations


def listToString(s):
 
    # initialize an empty string
    str1 = " "
 
    # return string
    return (str1.join(s))
     

list1 = input("")
# Split string into words
list2 = list1.split(" ")
#list3= list2[0]
list3 = list2[0].split(" ")
n = int(list2[1])

list4 = listToString(list3)

permutaion_list = list(permutations(list4,n))

permutaion_list.sort()

for tup in permutaion_list:
   print("".join(tup))
#n = int(list2[1])
#print(n)
