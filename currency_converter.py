def converter(currency_type, money):
    exchange_rates = {"USD": 0.00088, "JPY": 9.86, "CNY": 0.057, "EUR": 0.00074}
    if currency_type in exchange_rates:
        return money * exchange_rates[currency_type]
    else:
        return None


def main():
    print("통화 변환기 입니다.")
    converter_type = input(
        "어떤 나라의 통화로 변환하시겠습니까? (USD, JPY, CNY, EUR): "
    ).upper()

    if converter_type not in ["USD", "JPY", "CNY", "EUR"]:
        print("죄송합니다. 저희가 지원하지 않는 나라입니다.")
        return

    money = float(input("변환하실 원화 금액을 입력해주세요.: "))

    converted_amount = converter(converter_type, money)
    if converted_amount is not None:
        print(f"{money} 원은 {converted_amount} {converter_type}로 변환됩니다.")
    else:
        print("통화 변환에 실패했습니다. 다시 시도해주세요.")


if __name__ == "__main__":
    main()
