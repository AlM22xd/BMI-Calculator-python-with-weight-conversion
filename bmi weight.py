
while True:
    help = input("Welcome to BMI calculator: \n" "'start' to begin \n""'quit' to exit ").lower()
    if help == "quit":
        break
    elif help == "start":
        pass
    else:
        print("Please input a valid response")
        

    age = int(input("Please input your age "))

    height = float(input("Please input your height in meters "))

    weight = float(input("input the weight you wish to convert "))

    ty = input("What is the unit you are converting ").lower()

    kg = 0 

    if ty == "kg":
        kg = weight
        print(f"The weight in pounds is {weight * 2.20462:.2f} lbs")
        

    elif ty == "lb":
        print(f"The weight in kg is {weight / 2.20462:.2f} kgs")

        kg = weight / 2.20462 

    else:
        print("Please input a valid weight type")
        continue #-> 
    if age < 18 or age > 65:
        print("Error, age is invalid.") 
        continue
        
        
    else: 
        bmi = kg / height ** 2
        print (f" Your bmi is,{bmi:.3f}")

            #BMI = KG / m2 (meters squared)
                
        if bmi >= 18.5 and bmi <= 24.9:
            print("Your BMI is healthy!")
        elif bmi <= 18.5 and bmi >= 24.9: 
            print ("Your BMI is unhealthy!")

