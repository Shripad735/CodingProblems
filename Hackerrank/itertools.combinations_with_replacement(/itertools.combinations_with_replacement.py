from itertools import combinations_with_replacement

input_string = input("")

input_list = input_string.split(" ")

list1 = input_list[0]

n = int(input_list[1])


list2 = list(combinations_with_replacement(list1,n))

for i in range(len(list2)):
    list2[i] = sorted(list2[i])

list2.sort()


for i in range(len(list2)):
    print(''.join(list2[i]))

