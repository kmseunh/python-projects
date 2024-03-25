import datetime

import jwt


class JWTManager:
    """JWT를 생성하고 디코딩하는 클래스."""

    def __init__(self, secret_key):
        """JWTManager 클래스 생성자."""
        self.secret_key = secret_key

    def create_token(self, payload, expiration_time=None):
        """주어진 페이로드로 JWT 토큰을 생성합니다."""
        if expiration_time is None:
            expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

        token = jwt.encode(
            {"exp": expiration_time, **payload}, self.secret_key, algorithm="HS256"
        )
        return token

    def decode_token(self, token):
        """주어진 JWT 토큰을 디코딩하여 페이로드를 가져옵니다."""
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            return "Token has expired."
        except jwt.InvalidTokenError:
            return "Invalid token."


if __name__ == "__main__":
    # 비밀 키 설정
    SECRET_KEY = "your_secret_key_here"

    # JWT 매니저 생성
    jwt_manager = JWTManager(SECRET_KEY)

    # 페이로드 정의 (사용자 ID 등)
    payload = {"user_id": 123}

    # JWT 토큰 생성
    jwt_token = jwt_manager.create_token(payload)
    print("JWT Token:", jwt_token)

    # 생성된 JWT 토큰 디코딩하여 페이로드 가져오기
    decoded_payload = jwt_manager.decode_token(jwt_token)
    print("Decoded Payload:", decoded_payload)
