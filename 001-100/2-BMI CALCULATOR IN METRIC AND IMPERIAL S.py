#BMI CALCULATOR IN METRIC
height = float(input("Enter your height in meters: "))
weight = float(input("Enter Weight in KGs : "))
bmi= weight/(height**2)
if bmi>18.5 and bmi<24.9:
    print("your bmi is ",bmi," and comes in normal range")
elif bmi<18.5:
    print("your bmi is ",bmi," which is lower then normal limit")
elif bmi>24.9:
    print("your bmi is ",bmi," which is higher then normal limit")

