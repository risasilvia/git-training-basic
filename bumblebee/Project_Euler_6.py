batas = 100
b = 0
c = 0
for i in range (1,batas+1):
    k=i**2
    b+=k
    c+=i

d=c**2
e=d-b
print(b," ",d," ",e)