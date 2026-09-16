list = []
average = 0
sum = 0
for i in range (0,10):
    a = int(input("Enter integer : "))
    sum+=a
    list.append(a)

average  = sum/10
print("Average :",average)
print("Sum :",sum)
