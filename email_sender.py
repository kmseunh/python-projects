import smtplib
import ssl
from email.message import EmailMessage


def send_email(email_sender, email_password, email_receiver, subject, body):
    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.send_message(em)


if __name__ == "__main__":
    email_sender = input("보내는 이메일 주소를 입력하세요: ")
    email_password = input("이메일 비밀번호를 입력하세요: ")
    email_receiver = input("받는 이메일 주소를 입력하세요: ")

    subject = input("이메일 제목을 입력하세요: ")
    body = input("이메일 본문을 입력하세요: ")

    send_email(email_sender, email_password, email_receiver, subject, body)
