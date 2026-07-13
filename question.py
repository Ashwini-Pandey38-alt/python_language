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

# ''' Write a function prime(n) that returns true if  is a prime number and 
# False otherwise'''
# def prime(n):
#     for i in range (2,n):

#         if n%i==0:
#             return  False

#     return True


# print(prime(9))

 
# ''' Letʼs create a “
# Number Guessing Game
# ”.  Given a secret number (already 
# decided by you), write a program that asks the user to guess it and prints:
# "Too high" if the guess is above the number
# "Too low"  if the guess is below
# "Correct!" if the guess matche'''

# def guess():
#     a=15
#     while True:
#         n=int(input('enter the number value=='))
#         if n>a:
#             print( "too high ")
#         elif n<a:
#             print("too low")
#         else:
#             print('correct')
#             break


# guess()

# '''war to find the factorial of given number n '''
# def fact():
#     n=int(input('enter the number =='))
#     fact=1
#     for i in range (n,1,-1):

#         fact*=i

#     print(fact)

# fact()

# '''Ask the user for a string and check whether it is a palindrome or not. '''
# def rev():
#     word=input('enter the word=')
#     re=list(word)
#     if (re==re[::-1]):
#         print ('yes it an palandrom')
#     else:
#         print ('no is not an ')


# rev()

# '''Given a list of integers compute the average of all numbers in the list'''

# def avr():
#     list1=[]
#     x=int(input('enter the value for the length of the list1==='))
#     for  i in range (x):

#         num=int(input('enter the number for list==='))
#         list1.append(num)

#     count=0
#     sum=0
#     for k in list1:
#         sum+=k
#         count+=1


#     print(list1 , "avrage is==", (sum/count))

    
# avr()

# ''' Input two lists of integers from the user. Merge them into one list and sort the 
# result'''
# def merge():
#     n=int(input('enter the value for the length of the lists=='))
#     list1=[]
#     for i in range (n):
#         num1=int(input('enter the value of num1=='))
#         list1.append(num1)
#     list2=[]
#     for k in range (n):
#         num2=int(input('enter the value of num2=='))
#         list2.append(num2)
#     print(list1+list2)

# merge()

# '''use of dictionary .git()function'''
# item={ 5:"ashwini",'roll no. ':42,"sem":2 }
# item.git(5)

# '''Given a tuple of integers, create:
# • A tuple of all even numbers
# • A tuple of all odd number'''
# def t():
#     tup=(1,2,3,4,5,6,7,8,9,10)
#     te=()
#     to=()
#     l=list(te)
#     k=list(to)
    
#     for i in tup:
#         if ( i%2==0 ):

#             l.append(i)
#         else:

#             k.append(i)
#     te=tuple(l)
#     to=tuple(k)
#     print('tuple of all even value in given tuple',te)
#     print('tuple of all even value in given tuple',to)

# t()
'''WAP to show the length of list and also add new value in list'''
#Given a list of words:
words = ["apple", "banana", "kiwi", "cherry", "mango"]
len(words)
words.append('water')


