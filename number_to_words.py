class NumberToWords:
    def __init__(self, number):
        self.number = number

    def convert_to_words(self):
        UNITS = [
            "",
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        ]
        TEENS = [
            "",
            "eleven",
            "twelve",
            "thirteen",
            "fourteen",
            "fifteen",
            "sixteen",
            "seventeen",
            "eighteen",
            "nineteen",
        ]
        TENS = [
            "",
            "ten",
            "twenty",
            "thirty",
            "forty",
            "fifty",
            "sixty",
            "seventy",
            "eighty",
            "ninety",
        ]
        THOUSANDS = ["", "thousand", "million", "billion", "trillion"]

        words = []
        # 세 자리씩 끊어서 변환
        for i in range(0, len(str(self.number)), 3):
            chunk = int(str(self.number)[i : i + 3])
            chunk_words = []

            # 100의 자리
            if chunk // 100 > 0:
                chunk_words.append(UNITS[chunk // 100] + " hundred")
                chunk %= 100

            # 10의 자리
            if 10 <= chunk <= 19:
                chunk_words.append(TEENS[chunk % 10])
                chunk = 0
            elif chunk // 10 > 0:
                chunk_words.append(TENS[chunk // 10])
                chunk %= 10

            # 1의 자리
            if chunk > 0:
                chunk_words.append(UNITS[chunk])

            # 단위 추가
            if chunk_words:
                words.extend(
                    chunk_words + [THOUSANDS[len(str(self.number)) // 3 - (i // 3) - 1]]
                )

        return " ".join(words)


# 테스트
if __name__ == "__main__":
    number = int(input("숫자를 입력해주세요.: "))
    converter = NumberToWords(number)
    print(converter.convert_to_words())
