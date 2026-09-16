list = []
max = -1
for i in range (0,10):
    a = int(input("Enter integer : "))
    list.append(a)
min = list[0]
max = list[0]

for i in range (1,10):
    if list[i] < min:
        min = list[i]
    if list[i] > max :
        max = list[i]

print("Max : ",max)
print("Min : ",min)
print("Min : ",min)
