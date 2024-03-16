#write a program in python to find second smallest negetive element in the given list
lis = [22,-1,42,65,1,-4,6]
m1 = 999
m2 = 999
for i in lis:
  if i < m1:
    m2 = m1
    m1 = i
  elif m2 > i and m2 > m1:
    print(m1)