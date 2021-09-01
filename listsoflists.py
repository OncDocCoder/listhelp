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

ARow[1] = [2]
ARow[2] = [7]
ARow[3]= [4]
ARow[5]= [5]
ARow[6]= [9]
ARow[7]= [6]
BRow[0] = [4]
BRow[1] = [9]
BRow[3] = [2]
BRow[5] = [6]
BRow[7] = [5]
BRow[8] = [1]
CRow[2] = [1]
CRow[7] = [7]
DRow[0] = [7]
DRow[4] = [8]
DRow[7] = [6]
DRow[8] = [9]
ERow[2] = [9]
ERow[6] = [7]
FRow[0] = [1]
FRow[4] = [6]
FRow[8] = [5]
GRow[1] = [7]
GRow[6] = [5]
HRow[0] = [5]
HRow[1] = [1]
HRow[3] = [6]
HRow[5] = [7]
HRow[4] = [2]
HRow[7] = [3]
HRow[8] = [4]
IRow[1] = [4]
IRow[2] = [2]
IRow[3] = [8]
IRow[5] = [3]
IRow[6] = [6]
IRow[7] = [1]

Column0 = [ARow[0],BRow[0], CRow[0], DRow[0],ERow[0], FRow[0],GRow[0],HRow[0], IRow[0]]
Column1 = [ARow[1],BRow[1], CRow[1], DRow[1],ERow[1],FRow[1],GRow[1],HRow[1], IRow[1]]
Column2 = [ARow[2],BRow[2], CRow[2], DRow[2],ERow[2], FRow[2],GRow[2],HRow[2], IRow[2]]
Column3 = [ARow[3],BRow[3], CRow[3], DRow[3],ERow[3], FRow[3],GRow[3],HRow[3], IRow[3]]
Column4 = [ARow[4],BRow[4], CRow[4], DRow[4],ERow[4], FRow[4],GRow[4],HRow[4], IRow[4]]
Column5 = [ARow[5],BRow[5], CRow[5], DRow[5],ERow[5], FRow[5],GRow[5],HRow[5], IRow[5]]
Column6 = [ARow[6],BRow[6], CRow[6], DRow[6],ERow[6], FRow[6],GRow[6],HRow[6], IRow[6]]
Column7 = [ARow[7],BRow[7], CRow[7], DRow[7],ERow[7], FRow[7],GRow[7],HRow[7], IRow[7]]
Column8 = [ARow[8],BRow[8], CRow[8], DRow[8],ERow[8], FRow[8],GRow[8],HRow[8], IRow[8]]

print(Column0)
TotalbyColumns= [Column0, Column1, Column2, Column3, Column4, Column5, Column6, Column7, Column8]


# z = 0  #Get a list of the single digits and where they are in their lists.
# holder = []
# while z<9:
#       a = len(ARow[z])
#       if a==1:
#             holder.append(ARow[z])
#       z +=1
# print(holder) #holder is a list of single digits
# v = len(holder)
# m = 0
# while m < v: #this removes the single digits from the row
#       print(holder[m][0])
#       a = (holder[m][0])
#       t = 0
#       while t < 9:
#             if len(ARow[t])>1:
#                   if a in ARow[t]:
#                         ARow[t].remove(a)
#                         #print(t, ARow[t])
#                   t += 1
#             else:
#                   #print(ARow[t])
#                   t += 1
#       m +=1
# print(ARow)

###### Trying to get columns removed of singles####
z = 0  #Get a list of the single digits and where they are in their lists.
holder = []
while z<9:
      a = len(Column0[z])
      if a==1:
            holder.append(Column0[z])
      z +=1
print(holder, 'a') #holder is a list of single digits
v = len(holder)
m = 0
while m < v: #this removes the single digits from the row
      print(holder[m][0])
      a = (holder[m][0])
      t = 0
      while t < 9:
            if len(Column0[t])>1:
                  if a in Column0[t]:
                        Column0[t].remove(a)

                  t += 1
            else:
                  #print(ARow[t])
                  t += 1
      m +=1
print(Column0)







