"""def pattern(row,col):
    for i in range(row):
        if i==0 or i==row-1:
            print('*'*col)
        else:
            print('*'+" "*(col-2)+'*') 

pattern(4,5)"""

"""import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
timestamp=int(time.strftime('%H'))
print(timestamp)
timestamp=int(time.strftime('%M'))
print(timestamp)
if(timestamp==0 and timestamp==0 or timestamp<12 and timestamp==0):
    print('Good morning!')
elif(timestamp==12 and timestamp==0 or timestamp<16 and timestamp==0):
    print('Good afternoon!')
else:
    print('Good night!')"""
def pattern(row,col):
    for i in range(row):
        for j in range(i):
            print('*',end=' ') 
        print()  


def pattern(row,col):
    for i in range(row):
        j=0
        while(j<=i):
            print('*',end=' ') 
            j+=1
        print()  

pattern(5,5)
