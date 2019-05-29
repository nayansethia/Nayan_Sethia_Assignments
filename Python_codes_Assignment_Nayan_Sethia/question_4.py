import threading

def fileaccess(f):
    p=f.readlines()
    print("".join(p[-3:]))
    
f1=open("file1.txt", 'r')
f2=open("file2.txt", 'r')
f3=open("file3.txt", 'r')

t1=threading.Thread(target=fileaccess, args=(f1,))
t2=threading.Thread(target=fileaccess, args=(f2,))
t3=threading.Thread(target=fileaccess,args=(f3,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

