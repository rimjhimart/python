#weight calculator

weight = float(input("Enter your weight: "))
unit = input("Kilograms or pounds(K or L)?: ").lower()
if unit == "k":
  weight = weight * 2.205
  unit= "Lbs"
elif unit=="l":
  weight = weight/2.205
  unit = "Kgs"
else:
  print(f"{unit} is not valid")
print(f"your weight is {weight} {unit}.")