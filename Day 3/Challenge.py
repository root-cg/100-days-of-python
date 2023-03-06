# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm ?\n" ))


# if height > 120:
#     print("You can ride roallercoaster!")
# else:
#     print("Sorry, You can't Ride roallercoaster!")

#odd or Even


# number = int(input("Which Number do you want to check ?\n"))

# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")


#Rollercoaster with nested conditions

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm ?\n" ))
# age = int(input("what is your age?"))

# if height > 120:
#     print("You can ride roallercoaster!")
#     if age <= 12:
#         print("Please pay $5.")
#     elif( age > 12 and age <= 18):
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, You can't Ride roallercoaster!")



#BMI 2.0


# weight = float(input("enter your weight in m: \n"))
# height = float(input("enter your height in m: \n"))

# BMI_calc = round(weight / (height * height))

# if BMI_calc <= 18.5:
#     print(f"Your BMI is {BMI_calc}, you are underweight")
# elif (BMI_calc > 18.5 and BMI_calc <= 25):
#     print(f"Your BMI is {BMI_calc}, you have normal weight")
# elif (BMI_calc > 25 and BMI_calc <= 30):
#     print(f"Your BMI is {BMI_calc}, you are overweight")
# elif (BMI_calc > 30 and BMI_calc <= 35):
#     print(f"Your BMI is {BMI_calc}, you are obsee")
# else:
#     print(f"Your BMI is {BMI_calc}, you are clinically Obese Kindally seek Medical Attention!")



#LEAP YEAR CHECKER


# year = int(input("which year do you want to check? \n"))


# if (year % 4 == 0):
#     if (year % 100 ==0):
#         if (year % 400==0):
#             print("This is a leap year!")
#         else:
#             print("This is Not a leap year!")
#     else:
#         print("This is a leap year!")

# else:
#     print("This is NOT a leap year!")



#Roller Coaster with Multiple if Conditons

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm ?\n" ))
# age = int(input("what is your age?"))
# bill=0

# if height > 120:
#     print("You can ride roallercoaster!")
#     if age <= 12:
#         bill=5
#         print("Children pay $5.")
#     elif( age > 12 and age <= 18):
#         bill=7
#         print("Youth pay $7.")
#     else:
#         bill=12
#         print("Adult pay $12.")
    
#     want_pic = (input("Do you want click your Picture? It will cost additional $3  Y or N... \n"))
#     if (want_pic.lower() =='y'):
#         bill += 3
    
#     print(f"Your final amount is {bill}")

# else:
#     print("Sorry, You can't Ride roallercoaster!")

#Python Pizza

# print("Welcome to Python pizza Deliveries!")
# size = input("What size pizza do you want? S, M, Or L \n")
# add_pepperoni = input("Do you want Pepperoni? Y Or N \n")
# extra_cheese = input("Do you want extra cheese? Y or N \n")


# small_pizza=15
# medium_pizza=20
# large_pizza=25
# pep_sm = 2
# pep_md_lg =3 
# extra_chese = 1

# tracker=0


# if size.capitalize() == 'S':
#     tracker=small_pizza
#     if add_pepperoni.capitalize() == "Y":
#         tracker += pep_sm
# elif size.capitalize() == 'M':
#     tracker = medium_pizza
#     if add_pepperoni.capitalize() == "Y":
#         tracker += pep_md_lg
# elif size.capitalize() == 'L':
#     tracker = large_pizza
#     if add_pepperoni.capitalize() == "Y":
#         tracker += pep_md_lg



# if extra_cheese.capitalize() == "Y":
#     tracker +=extra_chese

# print(f"Your final bill is: {tracker} ..Enjoy your meal :).")


#logical Operators with rollarcoaster

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm ?\n" ))
age = int(input("what is your age?"))
bill=0

if height > 120:
    print("You can ride roallercoaster!")
    if age <= 12:
        bill=5
        print("Children pay $5.")
    elif( age > 12 and age <= 18):
        bill=7
        print("Youth pay $7.")
    elif(age > 18 and age<45):
        bill=12
        print("Adult pay $12.")
    elif(age >= 45 and age <= 55):
        bill=0
        print("Adult pay $0.")
    
    want_pic = (input("Do you want click your Picture? It will cost additional $3  Y or N... \n"))
    if (want_pic.lower() =='y'):
        bill += 3
    
    print(f"Your final amount is {bill}")

else:
    print("Sorry, You can't Ride roallercoaster!")