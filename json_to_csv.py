import csv
import json


def load_json(json_file):
    """JSON 파일을 읽어서 데이터를 반환하는 함수"""
    with open(json_file, "r", encoding="utf-8") as f:
        return json.load(f)


def save_csv(data, csv_file):
    """데이터를 CSV 파일에 저장하는 함수"""
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        # CSV 파일의 헤더를 작성
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        # 데이터를 CSV 파일에 작성
        writer.writerows(data)


def json_to_csv(json_file, csv_file):
    """JSON 파일을 CSV 파일로 변환하는 함수"""
    # JSON 파일을 읽기
    data = load_json(json_file)
    # CSV 파일에 데이터 저장
    save_csv(data, csv_file)


# JSON 파일 경로
json_file = "data.json"

# CSV 파일 경로
csv_file = "data.csv"

# JSON 파일을 CSV로 변환
json_to_csv(json_file, csv_file)

print("CSV 파일이 생성되었습니다.")
