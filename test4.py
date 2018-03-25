
# Collects the user's input for the prompt "What is your name?"
name = input("What is your name? ")

# Collects
neighborname = input("What is your neighbor's name? ")

# Collects the user's input for the prompt "How old are you?" and converts the string to an integer
months = int(input("How namy months have you been coding?"))

neighbormonths = int(input("How many months has " + str(neighborname) + " been coding?"))
# Collects the user's input for the prompt "Is this statement true?" and converts it to a boolean
totalmonths = int(months) + (neighbormonths)
# Creates three print statements that to respond with the output
print(str(name) + " has been coding for " + str(months) + ' months')
print(str(neighborname) + " has been coding for " + str(neighbormonths) + " months.")
print("Your combined coding experience is " + str(totalmonths) + " months.")
