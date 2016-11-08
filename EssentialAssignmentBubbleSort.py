
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                sorted = False
        print sorted

        if sorted:
            break
alist = [3,2,1]
bubbleSort(alist)
print(alist)

