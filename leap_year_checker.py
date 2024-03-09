def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


def main():
    print("윤년 검사기입니다.")
    year = int(input("확인할 년도를 입력해주세요. (ex 2024): "))

    if is_leap_year(year):
        print(f"{year}는 윤년입니다.")
    else:
        print(f"{year}는 윤년이 아닙니다.")


if __name__ == "__main__":
    main()
