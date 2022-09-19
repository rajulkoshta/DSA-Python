# problem : self sufficient  : https://prepinsta.com/infytq-previous-year-papers/coding-questions/question-2/


# def sol(n,earn,cost):
#     sum=0
#     for i in range(n):
#         sum += cost[i]-earn[i]
#     return sum

# print(sol(3,[3,4,2],[5,3,4]))

#--------------------------------------------------

# problem : parralel columbus : https://prepinsta.com/infytq-previous-year-papers/coding-questions/question-3/


def findTime(train_A,N,t):
    arr = []
    train_B = [N]
    train_B[0] = 0.00
    for i in range(0,N-1):
        train_B[i] = train_A[i-1] - train_A[i]
    it = int(t)
    if (t >= 0.0 and t <= 24.0 and (t - it) <= 60.0):
        for i in range(0,6):
            x = t + train_B[i]
            ix = int(x)
            if x-ix >= 0.60:
                x = x+ 0.40
            if x > 24.00:
                x = x - 24.0
            arr.append(x)    
        return arr
    else:
        return "Invalid Input"

train_A= [10.00, 10.04, 10.09,10.15, 10.19, 10.22 ]
N = len(train_A)
t = 11.00
res = findTime(train_A, N, t)
print(res)
