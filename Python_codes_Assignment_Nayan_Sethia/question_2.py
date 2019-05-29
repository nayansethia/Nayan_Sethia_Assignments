def bs(a,left,right,ele):
    if left<=right:
        mid=(left+right)//2
        if ele==a[mid]:
            return mid
        elif ele>a[mid]:
            return bs(a,mid+1,right,ele)
        else:
            return bs(a,left,mid-1,ele)
    else:
        return -1
        
while 1:
    print("Enter the number of elements you wish for your list")
    n=int(input())
    print("Enter elements one by one in sorted form:")
    l=[]
    for i in range(n):
        print("Enter the %d indexed element of list" %i)
        l.append(int(input()))

    k=sorted(l)
    if k!=l:
        print("for binary search you can only enter sorted list, otherwise you will lose the actual index of the element after sorting")
        print("Reenter the list")
        continue
    else:
        break
              
print("Here is the list entered by you")
print(l)

print("Enter the element you want to search in your list")
e=int(input())
returnvalue=bs(l,0,n-1,e)
if returnvalue==-1:
    print("Element not found")
else:
    print("index of the element is : %d" %returnvalue)
