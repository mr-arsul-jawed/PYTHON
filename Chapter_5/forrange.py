## range(): Range functions return a swqquesnce of number, starting from 0 by default, and increments by 1 (by default, and stops before a specified number.
                                                                                                
# range( start?, stop, step?)

# #EXAMPLE:1
# for i in range(10): #here 10 is range(stop)
#     print(i)       


# #EXAMPLE:2
# for i in range(2,10): #here: 2-start and 10-stop is range(start, stop)
#     print(i)
# 
# for i in range(2,10,2): #here: 2-start or 10-stop and 2-step is range(start,stop,step)
    # print(i)     

# for i in range(2,10,1):
#     print(i)

#Method: 1
Num = [1,2,3,4,5,6,7,8,9,10,11]

Even = []
Odd = []
# for i in range(1,12):
#     if(i%2 == 0):
#       Even.append(i)
#     elif(i%2 != 0):
#         Odd.append(i)
# print("Even Numbers are: ",Even)
# print("Odd Numbers are: ",Odd)

#Method:2
for i in range(len(Num)):
    
 if Num[i] %2==0:
   Even.append(Num[i])
 elif(Num[i] %2 != 0):
    Odd.append(Num[i])
  
print("Even Numbers are: ",Even)
print("Odd Numbers are: ",Odd)
