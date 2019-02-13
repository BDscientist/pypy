
def sum(a,b):
    sum=0;
    for i in range(a,b):
        sum = sum+i
    return sum


print("a와 b를 입력하시오")
print("=======================================")
print(sum(1,11))

print("=======================================")


def find_max(a):
    n= len(a)
    max_v=a[0]
    for i in range(1,n):
        if a[i]>max_v:
            max_v = a[i]
    return max_v

print("======================================")

c=[90,80,100,123,11,23,45,67]
print(find_max(c))

print("========================================")
def find_max2(a):
    n= len(a)
    max_v=a[0]
    for i in range(1,n):
        if a[i]>max_v:
            max_v = a[i]
    return max_v,i

v=[1,2,3,10]
print(find_max2(v))

print("===========================================")

def find_min(a):
    n=len(a)
    min_v=a[0]
    for i in range(1,n):
        if a[i]<min_v:
            min_v =a[i]
        return min_v,i

a1=[1,2,3,45,6,90,1000]
print(find_min(a1))

print("=========================================")



def fin (a):
    n=len(a)
    sum=set()
    for i in range(0,n):
        a[i] = a[i]/10000000
        sum.add(a[i]) 
    return sum    
    
v=[100000000,200000000,300000000]
print(fin(v))




print("=================================")

def find_same_name(a):
    n = len(a)                   
    result = set()                 
    for i in range(0, n -1):       
        for j in range(i + 1, n):  
            if a[i] == a[j]:     
                result.add(a[i])   
    return result

 

name = ["Tom", "Jerry", "Mike", "Tom"] 

print(find_same_name(name))

name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]

print(find_same_name(name2))


