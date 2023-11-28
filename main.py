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
                    - Consider incorporating healthy fats, protein-rich foods, and a variety of fruits and vegetables into the diet.
                    - Collaborate with a registered dietitian to ensure nutritional needs are met.
                    - Rule out any medical conditions contributing to low weight.
                    - Focus on lean protein sources such as poultry, fish, and lean meats.
                    - Include whole grains like quinoa, brown rice, and oats.
                    - Incorporate healthy fats from sources like olive oil, avocados, and nuts.""")
          elif blood_type == "a":
            print("""
                    You are advised to:
                    - Consult with a healthcare professional to identify potential underlying causes of low weight.
                    - Develop a balanced and nutrient-dense meal plan to support weight gain.
                    - Collaborate with a registered dietitian to ensure nutritional needs are met.
                    - Rule out any medical conditions contributing to low weight. 
                    - Include lean protein sources such as fish, poultry, tofu, and legumes.
                    - Incorporate whole grains like quinoa, brown rice, and oats for energy.
                    - Include sources of healthy fats, such as avocados, nuts, and olive oil.
                    """)
        
