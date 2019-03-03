listStart = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(listStart)):
    if listStart[i]%2==0:
        listStart[i]/=4
    else:
        listStart[i]*=2
print(listStart)