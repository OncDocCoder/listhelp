a = (['cat', 'dog', 'bear'], ['pizza', 'pie', 'cookie'])
#print(a)
#print(a[1])
#print(a[1][0])
del a[1][0]
#print(a)

b= ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9])
#print(a)
#print(b[1])
#print(b[1][0])
del b[1][0]
#print(b)

b= ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9])
#print(a)
#print(b[1])
#print(b[1][0])
#b[1][0]= 32
#print(b)

b= ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9])
q = 4
z = 2
newbie = []
holder = []
for x in range (9):
    if b[0][x] == q or b[0][x] == z:
        holder.append(b[0][x])
    else:
        newbie.append(b[0][x])

print(holder)
print(newbie)
b = (holder, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(b)

ARow= [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],\
      [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],\
      [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
BRow= [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],\
      [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],\
      [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
CRow= [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],\
      [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],\
      [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
DRow= [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],\
      [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],\
      [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
ERow= [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],\
      [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],\
      [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
FRow= [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],\
      [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],\
      [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
GRow= [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],\
      [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],\
      [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
HRow= [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],\
      [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],\
      [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
IRow= [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],\
      [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],\
      [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
ARow[0] = [1]
ARow[2] = [8]
ARow[3]= [4]
ARow[4]= [3]
BRow[1] = [7]
BRow[4] = [5]
BRow[5] = [8]
BRow[8] = [6]
CRow[1] = [6]
CRow[6] = [9]
CRow[7] = [3]
CRow[8] = [8]
DRow[0] = [7]
DRow[3] = [1]
DRow[7] = [6]
ERow[1] = [5]
ERow[2] = [3]
ERow[3] = [7]
ERow[5] = [9]
ERow[6] = [1]
ERow[7] = [8]
FRow[1] = [4]
FRow[5] = [3]
FRow[8] = [9]
GRow[0] = [8]
GRow[1] = [2]
GRow[2] = [5]
GRow[7] = [7]
HRow[0] = [9]
HRow[3] = [6]
HRow[4] = [2]
HRow[7] = [4]
IRow[4] = [7]
IRow[5] = [1]
IRow[6] = [2]

# for item in ARow:
#      a = len(ARow[item])
#      print(a)
z = 0  #Get a list of the single digits and where they are in their lists.
holder = []
while z<9:
      a = len(ARow[z])
      if a==1:
            holder.append(ARow[z])
      z +=1
print(holder) #holder is a list of single digits
v = len(holder)
m = 0
while m < v:
      print(holder[m][0])
      m +=1







