import re


n = input("")
n1 = int(n)

for i in range(n1):
  str = input()
  try:
    re.compile(str) 
    print(True)
  except re.error:
    print(False)
    
  
