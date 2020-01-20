def partition(arr,low,high):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            a[i],a[j]=a[j],a[i]
        arr[j],arr[pivot]=arr[pivot],arr[j]
    return i+1
    
def quicksort(arr,low,high):
    pivot=partition(arr,low,high)
    partition(arr,0,pivot-1)
    partition(arr,pivot+1,high)
    print(arr)    
    

while True:
    print("ENTER CHOICE:")
    print("a.enter array \n b.stop")
    choice=input()
    if choice=='a':   
        while True: 
            arr=[]   
            n=input("enter a no:")
            if n=='stop':
                break
            else:
                arr.append(int(n))
        quicksort(arr,0,len(arr)-1)
        
    elif choice=='b':
            break
        
    else:
            print("INVALID OPTION")
