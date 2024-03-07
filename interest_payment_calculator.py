def calculate_interest_payment(principal, annual_interest_rate, loan_term_years):
    # 연이자율을 월 이자율로 변환
    monthly_interest_rate = annual_interest_rate / 12 / 100
    # 대출 기간(월)
    loan_term_months = loan_term_years * 12

    # 월별 지불 정보를 저장할 리스트 생성
    monthly_payments = []

    remaining_principal = principal

    # 각 월에 대한 이자 및 총 지불액 계산
    for month in range(loan_term_months):
        # 이번 달에 지불할 이자 계산
        interest_payment = remaining_principal * monthly_interest_rate
        # 이번 달에 상환할 원금 계산
        principal_payment = principal / loan_term_months
        # 총 지불액 계산
        total_payment = interest_payment + principal_payment
        # 잔여 원금 갱신
        remaining_principal -= principal_payment

        # 월별 지불 정보를 리스트에 추가
        monthly_payments.append(
            {
                "month": month + 1,
                "interest_payment": interest_payment,
                "principal_payment": principal_payment,
                "total_payment": total_payment,
                "remaining_principal": remaining_principal,
            }
        )

    return monthly_payments


if __name__ == "__main__":
    # 사용자 입력 받기
    principal = float(input("대출 원금을 입력하세요: "))
    annual_interest_rate = float(input("연이자율을 입력하세요(예: 5.0): "))
    loan_term_years = int(input("대출 기간(년)을 입력하세요: "))

    # 이자 및 상환액 계산
    monthly_payments = calculate_interest_payment(
        principal, annual_interest_rate, loan_term_years
    )

    # 결과 출력
    print("\n월   이자   상환원금   총지불액   잔여원금")
    for payment in monthly_payments:
        # 잔여 원금이 0보다 작으면 0으로 설정
        if payment["remaining_principal"] < 0:
            payment["remaining_principal"] = 0

        print(
            "{month:2d}   {interest_payment:.2f}    {principal_payment:.2f}     {total_payment:.2f}    {remaining_principal:.2f}".format(
                **payment
            )
        )
