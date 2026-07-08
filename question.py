# print("hello world")

# '''Ask the user to enter two integers and one float. Convert them all to floats 
# and print their average.'''
# n1=int(input("enter the value of the number n1==="))
# n2=float(input("enter the value of the number n2==="))
# n3=int(input("enter the value of the number n3==="))
# a=float(n1)
# b=float(n2)
# c=float(n3)
# avg=(a+b+c)/3
# print(avg)

# ''' Ask the user for a temperature in Celsius (string input). Convert it to , 
# then calculate and print temperature in Fahrenheit.'''
# temp=input("enter the value of the temp===")
# tempCal=float(temp)
# tempFah=(tempCal*(9/5))+32
# print(tempFah)

# '''Take the radius ( ) as user input and print the area.'''
# r=float(input("enter the radius of circle===="))
# area=3.14*(r**2)
# print(area)


# '''Ask the user for:  Principal (P), Rate (R), Time (T). Convert all to float and 
# compute simple interest: '''
# P=float(input("enter the value of Principal=="))
# R=float(input("enter the value of rate =="))
# T=float(input("enter the value of time=="))
# simple_intrest=(P*R*T)/100
# print(' so the simple_intrest is ==',simple_intrest)




# def raa():
#     i=1
#     while (i<=5):
#         print("hello world")
#         i+=1

# raa()
# print("out of loop now")

# ''' Write a program that takes salary as input. Using conditional statements, 
# calculate the  final tax rate based on these rules• 
# If salary < 30,000 → 5%
# • 
# If salary is 30,000–70,000 → 15%
# • 
# If salary > 70,000 → 25%'''


# def final_tax():
#     salary=float(input('enter the salary =='))
#     if (salary==30000):
#         print ("you have to pay 5% tax")
#     elif (salary>=30000 or salary<=70000):
#         print(" you have to pay 15 % tax ")
#     elif(salary==70000):
#         print (" you have to pay 25 % tax")

# final_tax()


# '''Write a function that takes two integers  and  and prints all even 
# numbers between them (inclusive)'''

# def even():
#     a=int(input("entre the value for a "))
#     b=int(input("entre the value for b "))
#     for i in range (a,b+1):
#         if (i%2==0):

#             print(i)
#         else:
#             print(" ")



# even()




# '''Write a function to return the number of digits in a number,n'''
# def di():
#     n=str(input("enter the value of n == "))
#     count=0
#     for i in n:
#         count+=1

#     print(count)


# # di()
# """Write a function to return the sum of the digit of number n """
# def sum():
#     n = input("enter the value of n (only 3 digit) == ")
    
    
#     a = int(n[0])
#     b = int(n[1])
#     c = int(n[2])
    
#     sum = a + b + c
#     print(sum)

# sum()
# '''. Write a program to print all numbers from 1 to 100 that are divisible by both 3 
# and 5.'''
# def div():
#     a=1
#     b=100
#     for i in range(a,b+1):
#         if (i%3==0 and i%5==0):
#             print (i)
#         else:
#             print("")


# div()

''' Write a function prime(n) that returns true if  is a prime number and 
False otherwise'''
def prime(n):
    for i in range (2,n):

        if n%i==0:
            return  False

    return True


print(prime(9))

 
 