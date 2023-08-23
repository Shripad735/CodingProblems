from itertools import combinations

input_string = input("")

input_list = input_string.split(" ")

list1 = input_list[0]

n = int(input_list[1])

list4 = sorted(list(list1))
for i in range (len(list4)):
    print(''.join(list4[i]))

for i in range(2,n+1):
    list2 = list(combinations(list1,i))
    for i in range(len(list2)):
        list2[i] = sorted(list2[i])
    list2.sort()
    for i in range(len(list2)):
        print(''.join(list2[i]))

