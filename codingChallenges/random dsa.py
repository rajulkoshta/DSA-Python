# s='1101'
# i=0
# for x in s:
#     i = i*2 + int(x)
# print(i) 


# f1 = 1
# f2 = 2

# def f(n):
#     if n<3:
#         return n
#     return f(n-1)+(2*f(n-2))+(3*f(n-3))

# print(f(10))    


# def f(n):
#     for i in range(2,n//2):
#         if n%i==0 :
#             return False
#         else:
#             return True        

# if f(5)==True:
#     print("prime")
# else:
#     print("notprime")        

# def f(n):
#     if n < 2:
#         return n
#     return n * f(n-1)   
# print(f(6))

# def fsort(l):
#     for end in range(len(l),0,-1):
#         max = end
#         for i in range(end):
#             if l[i] > l[max]:
#                 max=i
#         l[max] , l[end] = l[end] , l[max]
#     return l 
# print(fsort([4,3,5,2,9,7,8]))    
# 


def show_excitement():
    string = "I am super excited for this course!"
    i=1
    while(i<5):
        string = string + i + " "
        i+=1
    return string
    
print(show_excitement())