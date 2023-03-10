#!/usr/bin/env python
# coding: utf-8

# In[58]:


#  import numpy as np
# def get_series(n):
    
# #     a[i]=0
#     for i in range(n):
#         a=[]
#         a[0]=0
#         a[1]=1
#         a[i+2]=a[i]+a[i+1]
#         a.append(int(a[i+2]))
        
#     print(a)
#     list_array = list(np.arange(1,n))
#     print(list_array)
num = 10
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2)
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3)

print()
 

    


# In[ ]:





# In[ ]:





# In[ ]:





# 

# In[38]:


R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
 
matrix = []
print("Enter the entries rowwise:")
 
# For user input
for i in range(R):         
    a =[]
    for j in range(C):      
         a.append(int(input()))
    matrix.append(a)
 
# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
    print()

#transpose of matix
for i in range(R):
    for j in range(C):
#         matrix[i][j]=matrix[j][i]
#         matrix[j][i]=matrix[i][j]
        print(matrix[j][i], end = " ")
    print()


# def count_ways(N):
#    dp = [0] * (N + 1)
#     dp[0] = 1
# 
#     for i in range(1, N + 1):
#         if i >= 1:
#             dp[i] += dp[i-1]
#         if i >= 3:
#             dp[i] += dp[i-3]
#         if i >= 5:
#             dp[i] += dp[i-5]
# 
#     return dp[N]

# In[ ]:




