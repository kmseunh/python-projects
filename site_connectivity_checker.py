import re

import requests


def site_request_check(url):
    print("사이트 연결을 확인중입니다..")
    response = requests.get(url)

    if response.status_code == 200:
        print("사이트 연결이 가능합니다.")
    else:
        print("사이트 연결이 불가능합니다.")


def url_check(url):
    pattern = r"(http|https)://(www\.)?[a-zA-Z0-9]+\.(com|net|org|edu|gov|mil|co\.kr)"

    if re.match(pattern, url):
        print("유효한 URL 양식입니다.")
        site_request_check(url)
    else:
        print("유효하지 않은 URL 양식입니다.")


if __name__ == "__main__":
    print("사이트 연결 검사기에 오신 것을 환영합니다.")
    input_site = input("연결을 확인할 사이트를 입력해주세요. : ")

    url_check(input_site)
