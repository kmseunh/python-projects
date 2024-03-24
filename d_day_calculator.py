from datetime import datetime


class DDayCalculator:
    def __init__(self):
        pass

    def calculate_d_day(self, target_date):
        today = datetime.now().date()
        delta = target_date - today
        return delta.days

    def get_target_date(self):
        year = int(input("목표 날짜의 연도를 입력하세요 (YYYY): "))
        month = int(input("목표 날짜의 월을 입력하세요 (MM): "))
        day = int(input("목표 날짜의 일을 입력하세요 (DD): "))
        return datetime(year, month, day).date()

    def run(self):
        target_date = self.get_target_date()
        d_day = self.calculate_d_day(target_date)

        if d_day > 0:
            print(f"D-{d_day}일 남았습니다.")
        elif d_day == 0:
            print("오늘이 목표 날짜입니다!")
        else:
            print(f"D+{abs(d_day)}일 지났습니다.")


if __name__ == "__main__":
    calculator = DDayCalculator()
    calculator.run()
