print("LINEAR SEARCH")
n = int(input("Enter no. of students who attended training: "))
ls = []
for i in range(n):
    rn = int(input("Enter roll no. of students: "))
    ls.append(rn)
print(ls)

s = int(input("Enter element to be searched:"))
for i in range(n):
    if s == ls[i]:
        print(f"Roll no. found at index{i}")