# A For loop moves through a given range of numbers
# If only one number is provided it will loop from 0 to that number
x = "Yes"
while x == "Yes":

    for x in range(20):
        print(x)

    # If two numbers are provided then a For loop will loop from the first number up until it reaches the second number
    for x in range(30,50):
        print(x)

    # If a list is provided, then the For loop will loop through each element within the list
    for x in ["Peanut","Butter","Jelly","Time","Is","Now","Beer"]:
        print(x)

    # A While Loop will continue to loop through the code contained within it until some condition is met
 
    print("Whee! Merry-Go-Rounds are great!")
    x = input("Would you like to go on the Merry-Go-Round again? ")