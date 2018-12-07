
n=int(input("Amount of grades entering?: "))
a=[]
for i in range(0,n):
    elem=int(input("Enter Dave's grade: "))
  a.append(elem)
avg=sum(a)/n
print("Dave grade average",round(avg,2))

for i in range(0,n):
    elem=int(input("Enter Sara's grade: "))
    a.append(elem)
avg=sum(a)/n
print("Sara's grade average",round (avg,2))


