print("Welcome to BodyMath: A smart BMI calculator")
print("This application is designed to assess Body-Mass-Index, a common metrix used for gauging body weight in relation to height")
print("\n1. Add patient\n2. Enter your details\n3. Display patient\n4. Medical advice\n5. Save and Exit")
            choice = input("Enter your choice (1-5): ")

def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category

def dietary_advise(category, blood_type, return_advice=False):
    category_lower = category.lower()
    advice = ""

    if category_lower == "underweight":
          if blood_type == "o":
            print("""You are advised to:
                    - Consult with a healthcare professional to identify potential underlying causes of low weight.
                    - Develop a balanced and nutrient-dense meal plan to support weight gain.
                    - Consider incorporating healthy fats, pr
        
