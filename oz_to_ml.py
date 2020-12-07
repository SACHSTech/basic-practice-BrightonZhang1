recipe_ounces = float(input("Enter the amount of fluid in ounces: "))
servings = float(input("Enter the number of people to serve: "))

print("You will need", (recipe_ounces*29.5735) * (servings/4), "ml")

