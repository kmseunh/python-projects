def decimal_to_binary(decimal):
    """십진법을 이진법으로 변환합니다."""
    return bin(decimal).replace("0b", "")


def binary_to_decimal(binary):
    """이진법을 십진법으로 변환합니다."""
    return int(binary, 2)


def main():
    while True:
        choice = input(
            "변환을 선택하세요 (1: 십진수에서 이진수로, 2: 이진수에서 십진수로): "
        )

        if choice == "1":
            try:
                decimal_input = int(input("십진수를 입력하세요: "))
            except ValueError:
                print("정수를 입력하세요.")
            binary_output = decimal_to_binary(decimal_input)
            print("이진수 표현:", binary_output)
        elif choice == "2":
            try:
                binary_input = input("이진수를 입력하세요: ")
                decimal_output = binary_to_decimal(binary_input)
                print("십진수 표현:", decimal_output)
            except ValueError:
                print("올바른 이진수를 입력하세요.")
        elif choice.lower() == "q":
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바를 숫자를 입력해 주세요")


if __name__ == "__main__":
    main()
