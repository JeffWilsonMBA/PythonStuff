
name = input("What is your name? ")

print("Hi, " + str(name))
print("")
age = input("How old are you? ")
print("")
# Run Conditionals
if int(age) < 10:
    print("You are just a baby!")

elif int(age) >= 10 and int(age) < 21: 
    print("Ah....you have a few years on you but you still cannot have a beer!")

elif int(age) >= 21:
    print("You are an old fart.")
 
else:
  pass
