tup=list(tuple(map(int,input("Enter tuples with space a b: ").split()))for r in range(int(input("Enter number of pairs: "))))
lst = len(tup)
print("The list given is: ",tup)
for i in range(0, lst): 
        for j in range(0, lst-i-1): 
            if (tup[j][-1] > tup[j + 1][-1]): 
                temp = tup[j] 
                tup[j]= tup[j + 1] 
                tup[j + 1]= temp
                continue
print("The arranged list is: ",tup)
