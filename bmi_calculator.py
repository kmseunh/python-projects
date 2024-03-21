class BMICalculator:
    def __init__(self, weight, height):
        self.weight = weight  # 몸무게 (kg)
        self.height = height  # 키 (m)

    def calculate_bmi(self):
        """
        BMI를 계산하는 메서드
        """
        return self.weight / (self.height**2)

    @staticmethod
    def interpret_bmi(bmi):
        """
        BMI를 해석하여 결과를 반환하는 정적 메서드
        """
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obesity"


def get_user_input():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    return weight, height


def main():
    weight, height = get_user_input()

    bmi_calculator = BMICalculator(weight, height)
    bmi = bmi_calculator.calculate_bmi()
    bmi_category = BMICalculator.interpret_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are {bmi_category}")


if __name__ == "__main__":
    main()
