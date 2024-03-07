class Quiz:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check_answer(self, user_answer):
        return self.answer == user_answer


def run_quiz(questions):
    score = 0
    for question in questions:
        print(question.question)
        user_answer = input("정답을 입력해 주세요: ")
        if question.check_answer(user_answer):
            print("정답입니다.")
            score += 1
        else:
            print(f"틀렸습니다. 정답은 {question.answer} 입니다.")
        print()
    print("퀴즈가 종료되었습니다.")
    print(f"최종 점수는 {score}/{len(questions)}")


if __name__ == "__main__":
    quiz_questions = [
        Quiz("세계에서 가장 큰 강은 무엇일까요?", "아마존"),
        Quiz("태양계에서 가장 큰 행성은 무엇일까요?", "목성"),
        Quiz("아인슈타인의 상대성 이론은 무엇인가요?", "상대성 이론"),
        Quiz("파이썬의 창시자는 누구일까요?", "귀도 반 로섬"),
        Quiz("지구의 지름은 몇 킬로미터인가요?", "12742"),
    ]

    run_quiz(quiz_questions)
