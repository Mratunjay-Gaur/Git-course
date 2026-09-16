list = []
for i in range (0,5):
    a = int(input("Enter integer : "))
    list.append(a)

for i in range (0,len(list)):
    for j in range (0,i):
        if list[i] == list[j]:
            if i != j:
                list[j] = -1
print(list)