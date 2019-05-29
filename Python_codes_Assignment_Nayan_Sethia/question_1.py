def lastelement(li):
    return li[-1]

i=0
l=[]

while 1:
    
    print("Enter the number of elements for this tuple")
    nt=input()
    if not nt.isdigit() or int(nt)<0:
        print("You are supposed to enter only positive no.s")
        continue
    nt=int(nt)
    
    t=[];
    for j in range(nt):
        print("Enter the %d  index of %d th tuple" %(j,i))
        t.append(int(input()))
    t=tuple(t)
    l.append(t)
    print("the final list of tuples entered by you look like this:")
    print(l)
    print("here is the sorted list of tuples in increasing order on the basis of last element of each tuple")
    l.sort(key=lastelement)
    print(l)
    print("Do you want to add more tuples, if yes press yes, otherwise press any other key")
    p=input().lower()
    if p=="yes":
        continue
    else:
       break
    i=i+1


                 
        
    
    
