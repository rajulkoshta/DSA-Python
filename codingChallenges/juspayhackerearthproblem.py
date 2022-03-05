arr=[]
N = int(input()) # N
for _ in range(0,N): # member ids
    arr.append(int(input()))

E = int(input()) # total possible edges
m={}
for _ in range(0,E):
    fol,foling = input().split()
    fol = int(fol)
    foling = int(foling)
f = int(input())
fing = int(input()) 

for keys,values in m.items():
    for val in values:
        if val == fing:
            print('%d' % keys)