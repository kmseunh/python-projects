import os


class StringSearcher:
    def __init__(self, directory):
        self.directory = directory

    def search_string_in_files(self, search_string):
        results = []
        for root, _, files in os.walk(self.directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        for line_number, line in enumerate(f, start=1):
                            if search_string in line:
                                # 튜플을 괄호로 묶어서 하나의 요소로 추가
                                results.append((file_path, line_number, line.strip()))
                except UnicodeDecodeError:
                    pass
        return results


if __name__ == "__main__":
    directory = input("검색할 디렉토리 경로를 입력하세요: ")
    search_string = input("검색할 문자열을 입력하세요: ")

    searcher = StringSearcher(directory)
    search_results = searcher.search_string_in_files(search_string)

    if search_results:
        print(f"'{search_string}'를 포함하는 파일들:")
        for result in search_results:
            print(f"{result[0]} - 라인 {result[1]}: {result[2]}")
    else:
        print("검색된 결과가 없습니다.")
