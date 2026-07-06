print("hello world")

#. Ask the user to enter two integers and one float. Convert them all to floats 
#and print their average.
n1=int(input("enter the value of the number n1==="))
n2=float(input("enter the value of the number n2==="))
n3=int(input("enter the value of the number n3==="))
a=float(n1)
b=float(n2)
c=float(n3)
avg=(a+b+c)/3
print(avg)

''' Ask the user for a temperature in Celsius (string input). Convert it to , 
then calculate and print temperature in Fahrenheit.'''
temp=input("enter the value of the temp===")
tempCal=float(temp)
tempFah=(tempCal*(9/5))+32
print(tempFah)

'''Take the radius ( ) as user input and print the area.'''
r=float(input("enter the radius of circle===="))
area=3.14*(r**2)
print(area)
