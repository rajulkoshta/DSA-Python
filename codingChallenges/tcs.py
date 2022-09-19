# def goldcoins(list1,n,k):
#     for i in range(n):
#         sum = list1[i]
#         if i+1<n:
#             for j in range (i+1,n):
#                 sum += list1[j]
#                 if sum == k:
#                     return i+1,j+1
#                     break
#                 if sum>k:
#                     break

# n,k = map(int , input().split())
# list1 = list(map(int,input().split()))[:n]
# print(*goldcoins(list1,n,k))

# def sumorProduct(a, b, c, op):
 
#     # Finding sum of roots
#     S = (-1 * b)/a
 
#     # Finding product of roots
#     P = c / a
 
#     if op == '+':
#         return int(S+P)
#     elif op == '*':
#         return int(S*P)


# print(sumorProduct(4,-16,8,'*'))


# def gcd(a,b):
     
#     # Everything divides 0
#     if (a == 0):
#         return b
#     if (b == 0):
#         return a
 
#     # base case
#     if (a == b):
#         return a
 
#     # a is greater
#     if (a > b):
#         return gcd(a-b, b)
#     return gcd(a, b-a)


# def superGCD(n):
#     res = 0
#     for i in range(1,n+1):
#         res += 2**i + gcd(i,n)
#     return res

# print(superGCD(6))


def gcd(a,b):

    # Everything divides 0
    if (a == 0):
        return b
    if (b == 0):
        return a
 
    # base case
    if (a == b):
        return a
 
    # a is greater
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)

# Function to find the farthest
# co-prime number over the range
def update(arr, n):

    # Traverse the array arr[]
    for i in range(n):
    
        # Stores the distance
        # between j and arr[i]
        d = 0

        # Stores the integer coprime
        # which is coprime is arr[i]
        coPrime = -1

        # Traverse the range [2, 250]
        for j in range(2, 251, 1):
        
            # If gcd of arr[i] and j is 1
            if (gcd(arr[i], j) == 1 and d < abs(arr[i] - j)):
            
                # Update the value of d
                d = abs(arr[i] - j)

                # Update the value
                # of coPrime
                coPrime = j

        # Update the value of arr[i]
        arr[i] = coPrime

    # Print the array arr[]
    for i in range(n):
        print(arr[i],end =" ")

# Driver Code
if __name__ == '__main__':
    arr = [60, 246, 75, 103, 155, 110]
    N = len(arr)
    update(arr, N)
    