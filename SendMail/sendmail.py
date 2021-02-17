import smtplib
from email.message import EmailMessage
import imghdr
import re

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")

message = EmailMessage()
message.set_content("코드라이언 수업으로 파이썬으로 메일 보낸당!")

message["Subject"] = "파이썬으로 메일 보내기"
message["From"] = "#####@gmail.com"
message["To"] = "******@gmail.com"

with open("PaintJS🎨.png","rb") as image:
    image_file = image.read()

image_type = imghdr.what('sendmail', image_file)
message.add_attachment(image_file, maintype='image', subtype=image_type)

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("#######@gmail.com", "#########")        # 보안으로 #처리
sendEmail("****@gmail.com")
smtp.quit()