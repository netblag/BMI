def BMI_calc(weight,height):
    bmi = weight / (height/100)**2
    return bmi

bmi = round(BMI_calc(80.5,181),2)

print(f"BMI: {bmi}")