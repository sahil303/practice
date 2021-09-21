num = int(input("Enter number:: "))
flag = 0
if num % 2== 0:
    flag = 1
    print("\nEven Number")
else:
    
    print("\nOdd Number")
    
if flag == 1:
    n = num
    sum = (n*(n+1))/2
    print("Sum of Even numbers upto ",num," is :",sum)
else:
    n = num
    sum = n**2
    print("Sum of Odd numbers upto ",num," is :",sum)

print("Thankyou")