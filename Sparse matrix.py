n=int(input("Enter no. of rows: "))
m=int(input("Enter no of columns: "))
mat=[]
for i in range(n):
  r=[]
  for j in range(m):
    num=int(input("enter elements: "))
    r.append(num)
  mat.append(r)
  print(mat)

sparse_mat=[]
for i in range(n):
  for j in range(m):
    if mat[i][j] != 0:
      temp=[]
      temp.append(i)
      temp.append(j)
      temp.append(mat[i][j])
      sparse_mat.append(temp)

print(f"\nsparse matrix: {sparse_mat}")

n=int(input("Enter no. of rows: "))
m=int(input("Enter no of columns: "))
mat2=[]
for i in range(n):
  r=[]
  for j in range(m):
    num=int(input("enter elements: "))
    r.append(num)
  mat2.append(r)
  print(mat2)

sparse_mat2=[]
for i in range(n):
  for j in range(m):
    if mat2[i][j] != 0:
      temp2=[]
      temp2.append(i)
      temp2.append(j)
      temp2.append(mat2[i][j])
      sparse_mat2.append(temp2)

print(f"\nsecond sparse matrix: {sparse_mat2}")

sum=[]
for i in range(n):
  add=[]
  for j in range(m):
    a= sparse_mat[i][j] + sparse_mat2[i][j]
    add.append(a)
  sum.append(add)
print(f'sum of sparse matrix: {sum}')