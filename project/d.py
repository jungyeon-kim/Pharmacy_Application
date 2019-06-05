import smtplib
from email.message import EmailMessage

smtp_gmail = smtplib.SMTP('smtp.gmail.com', 587)

smtp_gmail.ehlo()
smtp_gmail.starttls()
smtp_gmail.login('zoemfhs123@gmail.com', 'kjy341229!')

msg = EmailMessage()

# 제목 입력
msg['Subject'] = "제목입니다"

# 내용 입력
msg.set_content("내용입니다")

# 보내는 사람
msg['From'] = 'zoemfhs123@gmail.com'

# 받는 사람
msg['To'] = 'jisu0838@naver.com'

smtp_gmail.send_message(msg)