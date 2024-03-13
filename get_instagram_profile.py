import requests
from bs4 import BeautifulSoup


def get_instagram_profile(username):
    # 사용자명에 해당하는 인스타그램 프로필 페이지 URL
    url = f"https://www.instagram.com/{username}/"

    response = requests.get(url)

    if response.status_code == 200:
        # BeautifulSoup을 사용하여 HTML 파싱
        soup = BeautifulSoup(response.text, "html.parser")

        # 메타 태그에서 프로필 정보 추출
        meta_tags = soup.find_all("meta", attrs={"property": "og:description"})

        # 메타 태그를 순회하며 프로필 정보 추출
        for tag in meta_tags:
            content = tag.get("content")
            if content:
                # 추출된 정보를 쉼표를 기준으로 분리하여 팔로워 수, 팔로잉 수, 게시물 수 추출
                followers, following, posts = content.split(", ")
                return {
                    "사용자명": username,
                    "팔로워": followers,
                    "팔로잉": following,
                    "게시물": posts,
                }
    else:
        print("오류: 프로필 정보를 가져올 수 없습니다.")


if __name__ == "__main__":
    username = input("인스타그램 사용자명을 입력하세요: ")

    profile_info = get_instagram_profile(username)

    if profile_info:
        print("프로필 정보:")
        print(f"사용자명: {profile_info['사용자명']}")
        print(f"팔로워: {profile_info['팔로워']}")
        print(f"팔로잉: {profile_info['팔로잉']}")
        print(f"게시물: {profile_info['게시물']}")
