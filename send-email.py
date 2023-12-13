# Python 脚本自动发送邮件提醒

from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.header import Header


# 邮件配置
smtp_server = 'smtp.qq.com'         # 你的SMTP服务器地址，默认是qq邮箱的smtp的服务器地址smtp.qq.com
smtp_port = 587                     # SMTP服务器端口号: 456 or 587 （这个端口号可不是瞎编的）
smtp_username = 'erode1701@qq.com'  # 你的邮箱用户名
smtp_password = 'xxxxx'             # 你的邮箱授权码   （注意邮箱授权码不是邮箱登陆密码，需要你打开IMAP/SMTP服务）
sender = 'xxxxxxx@qq.com'           # 发件人邮箱地址
receiver = ['xxx@qq.com','xxxx@qq.com']   # 收件人邮箱地址

# 构建邮件
mail_title = '你的邮件标题'
mail_content = '你的邮件内容'
message = MIMEMultipart()
message['Subject'] = Header(mail_title,'utf-8')
message['From'] = sender
message['To'] = ";".join(receiver)
message.attach(MIMEText(mail_content, 'plain', 'utf-8')) # 邮件正文内容


# 1.添加文本文件附件
text_file = 'example/example.txt'
with open(text_file, 'rb') as file:
    attachment = MIMEText(file.read().decode('utf-8'))
    attachment.add_header('Content-Disposition', 'attachment', filename='example.txt')
    message.attach(attachment)

# 2.添加图片附件
image_file = 'example/example.jpeg'
with open(image_file, 'rb') as file:
    attachment = MIMEImage(file.read(), name='example.jpeg')
    attachment.add_header('Content-Disposition', 'attachment', filename='背景图.jpeg')
    message.attach(attachment)

# 3.添加Excel附件
excel_file = 'example/example.xlsx'
with open(excel_file, 'rb') as file:
    attachment = MIMEApplication(file.read(), name='example.xlsx')
    attachment.add_header('Content-Disposition', 'attachment', filename='example.xlsx')
    message.attach(attachment)

# 4.添加压缩包附件
zip_file = 'example/example.zip'
with open(zip_file, 'rb') as file:
    attachment = MIMEApplication(file.read(), name='example.zip')
    attachment.add_header('Content-Disposition', 'attachment', filename='example.zip')
    message.attach(attachment)

# 5.添加PDF附件
pdf_file = 'example/example.pdf'
# 读取PDF文件并将其附加到邮件中
with open(pdf_file, 'rb') as file:
    attachment = MIMEApplication(file.read(), name='example.pdf')
    attachment.add_header('Content-Disposition', 'attachment', filename='example.pdf')
    message.attach(attachment)

# 6.添加音频文件附件
audio_file = 'example/example.mp3'  # 替换为实际的音频文件路径
with open(audio_file, 'rb') as file:
    attachment = MIMEApplication(file.read(), name='example.mp3')
    attachment.add_header('Content-Disposition', 'attachment', filename='example.mp3')
    message.attach(attachment)

# 7.添加视频文件附件
video_file = 'example/example.mp4'  # 替换为实际的视频文件路径
with open(video_file, 'rb') as file:
    attachment = MIMEApplication(file.read(), name='example.mp4')
    attachment.add_header('Content-Disposition', 'attachment', filename='example.mp4')
    message.attach(attachment)



# 连接到SMTP服务器并发送邮件
try:
    smtp = SMTP_SSL(smtp_server)                  # ssl登录
    smtp.login(smtp_username,smtp_password)
    smtp.sendmail(sender,receiver,message.as_string())
    print('邮件发送成功')
except Exception as e:
    print(f'邮件发送失败: {str(e)}')
finally:
    smtp.quit()
