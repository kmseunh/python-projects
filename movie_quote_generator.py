def get_movie_quote(movie):
    quotes = {
        "A": "아직 {word1} 에게는 {word2}의 배가 남아 있사옵니다.",
        "B": "지금까지 이런 맛은 없었다. 이것은 {word1}인가 {word2}인가.",
        "C": "지금 내 {word1}이 그래. {word2}가 없네?",
    }
    return quotes.get(movie, "해당하는 영화 명대사가 없습니다.")


def main():
    print("원하는 영화 명대사를 선택해주세요")
    print("A: 명량")
    print("B: 극한직업")
    print("C: 베테랑")

    selected_movie = input("입력: ").upper()

    if selected_movie not in ["A", "B", "C"]:
        print("올바른 영화를 선택해주세요.")
        return

    famous_line = get_movie_quote(selected_movie)

    print(famous_line)

    print("단어를 채워주세요")
    word1 = input("word1: ")
    word2 = input("word2: ")

    line = famous_line.format(word1=word1, word2=word2)
    print(line)


if __name__ == "__main__":
    main()
