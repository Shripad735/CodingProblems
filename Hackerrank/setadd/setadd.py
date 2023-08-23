# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

s = set('')

for i in range(n):
  str = input()
  if str in s:
    continue
  else:
    s.add(str)

print(len(s))
    
