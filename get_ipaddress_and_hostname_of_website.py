import socket
from urllib.parse import urlparse


def get_host_ip(url):
    """
    URL에서 호스트의 IP 주소를 가져옵니다.
    """
    try:
        return socket.gethostbyname(url)
    except socket.gaierror as e:
        print("호스트를 해결하는 중 오류 발생:", e)
        return None


def extract_domain_and_host(url):
    """
    URL에서 도메인 이름과 호스트 이름을 추출합니다.
    """
    parsed_url = urlparse(url)
    domain_name = parsed_url.netloc.split(":")[0]
    ip_address = get_host_ip(domain_name)
    if "www." in domain_name:
        host_name = domain_name.split("www.")[-1]
    else:
        host_name = domain_name
    return domain_name, host_name, ip_address


def get_validated_url():
    """
    사용자로부터 URL을 입력받고, 필요에 따라 프로토콜을 추가하여 반환합니다.
    """
    url = input("URL을 입력하세요: ").strip()
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    return url


def main():
    url = get_validated_url()
    domain_name, host_name, ip_address = extract_domain_and_host(url)
    if ip_address:
        print("도메인 네임:", domain_name)
        print("호스트 네임:", host_name)
        print("IP 주소:", ip_address)


if __name__ == "__main__":
    main()
