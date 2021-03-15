Weight_kilo = float(input("Weight in kilo: "))
Height_meter = float(input("Height in meter: "))

BMI = Weight_kilo / Height_meter ** 2

print(f"BMI: {BMI}")

if BMI > 24:
    print(f"Result: {'Overweight'}")
    target_weight = Weight_kilo - 24 * Height_meter ** 2
    print(f"Target decrease in weight: {target_weight}")
elif BMI >= 18:
    print(f"Result: {'Normal'}")
    print("Keep it up!")
else:
    print(f"Result: {'Underweight'}")
    target_weight = 18 * Height_meter ** 2 - Weight_kilo
    print(f"Target increase in weight: {target_weight}")
