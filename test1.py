list1 = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
list2 = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
sym="0"
a=4
list1[a]=sym
b=0
for i in range(0, 3, 1):
    for j in range(0, 3, 1):
        list2[i][j] = list1[b]
        b+=1
for i in range(0,3,1):
    for j in range(0,3,1):
        if j<2:
           print(" ",list2[i][j]," ",end="|")
        else:
            print(" ",list2[i][j]," ",end=" ")
    print()
    if i<2:
        print("-----|-----|-----")
    else:
        print(" ")