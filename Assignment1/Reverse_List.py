list = []
n = int(input("Enter Size : "))
for i in range (0,n):
    a = int(input("Enter integer : "))
    list.append(a)

for i in range (0,n):
         a = list[i]
         b = (0-a)
         list[i] = list[b]
         list[b] = a

print(list)