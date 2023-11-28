Medical advice\n5. Save and Exit")
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.name = input("Enter your name: ")
                self.gender = input("Enter your gender: ")
                self.blood_type = input("Enter your blood type (O, A, B, AB): ").lower()
                self.age = input("Enter your age: ")
            elif choice == "2":
                weight = float(input("Enter your weight (kg): "))
                height = float(input("Enter your height (m): "))
                bmi, category = bmi_calculator(weight, height)
                print(f"Your BMI is {bmi:.2f}, and your category is {category}")
            elif choice == "3":
                self.display_patient_info()
            elif choice == "4":
                advice = dietary_advise(category, self.blood_type, return_advice=True)
                print(advice)
            elif choice == "5":
                self.save_to_file(bmi, category, advice)
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
