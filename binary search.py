noofstu = int(input("enter no. of students who attended training: "))
l = []
for i in range(noofstu):
    rno = int(input("enter roll no. of students in sorted order: "))
    l.append(rno)
print(l)
bsearch = int(input("enter roll no of student to be searched: "))
mid = int((0+noofstu-1)/2)
for i in range(noofstu):
    if l[mid] == bsearch:
        print(f"roll no found at position {i}")
        if l[mid] > bsearch:
          for i in range(mid, noofstu-1):
            if bsearch == l[i]:
              print(f"roll no found at position {i}")
        if l[mid] < bsearch:
          for i in range(0, mid-1):
            if bsearch == l[i]:
                print(f"roll no found at position {i}")