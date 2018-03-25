# The list of candies to print to the screen
pieList = ["Pecan", "Apple Crisp", "Bean", "Bancoffee", "Black Bun", "Blueberry", "Buko", "Burek", "Tamale", "Steak"]
# pieList.index = pieList.index + 1

# The list used to store all of the pies selected inside of
pieCart = []
print("Welcome to the House of Pies!!  Here is a list of pies.")

shopping = "y"
while shopping =="y":
    print("------------------------------------------")
    for pie in pieList:
        print("(" + str(pieList.index(pie) + 1) + ") " + (pie))
    selected = input("Which pie would you like to put into your cart? ") 
    pieCart.append(pieList[int(selected)])
    print("------------------------------------------")
    print("Nice choice.  I like " + pieList[int(selected) - 1] + " pie.")
    print("We will get that " + pieList[int(selected) - 1] + " right out to you.")
    shopping = input("Would you like to buy another pie? ")

print("Total pies purchased:  " + str(len(pieCart)))
print("You purchased the following pies:")
for pie in pieCart:
     print(pie)