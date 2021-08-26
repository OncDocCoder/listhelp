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



