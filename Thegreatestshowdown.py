n1= int(input("Enter a number please:  "))
n2 = int(input("enter a number please: "))
n3 = int(input("enter a number please: "))


if (n1 >= n2) and (n1 >= n3):
   num1 = n1 
elif (n2 >= n1) and (n2 >= n3):
   num1 = n2
else:
   num1 = n3


print("the largest number among",n1,",",n2,"and",n3,"is: ", num1)


if (n1 <= n2) and (n1 <= n3):
   num1 =n1
elif (n2 <= n1) and (n2 <= n3):
   num1 = n2
else:
   num1 = n3


print("The smallest number among",n1,",",n2,"and",n3,"is: ", num1)