# 🚨 Don't change the code below 👇
#number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#y = int(number)
#print(type(y))

#if y % 2 == 0:
 # print ("This is an even number.")
#else:
 # print ("This is an odd number.")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age?"))
  if age < 12 :
    print ("Please pay $5.")
    bill = 5
  elif age <= 18 :
    print ("Please pay $7.")
    bill = 7
  elif age < 22 :
    print ("Please pay $10. ")
    bill = 10
  else :
    print ("Please pay $12.")
    bill = 12
  
  photo_request = input("Do you want your photo taken? Y or N. ")
  #print(type(photo_request))

  if photo_request == "Y" :
    bill += 3
  print (f"Your final bill is {bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")



