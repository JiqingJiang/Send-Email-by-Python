# Python 脚本自动发送邮件提醒
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.header import Header

class Email:

    def __init__(self,smtp_username:str,smtp_password:str,receiver:list(str),smtp_server:str ='smtp.qq.com'):
        # 邮件配置
        self.smtp_server = smtp_server    # 你的SMTP服务器地址
        self.smtp_port = 587                # SMTP服务器端口号: 456 or 587
        self.smtp_username = smtp_username  # 你的邮箱用户名
        self.smtp_password = smtp_password  # 你的邮箱密码
        self.receiver = receiver
        self.message = MIMEMultipart()
        self.message['From'] = self.smtp_username
        self.message['To'] = ";".join(receiver)

    def set_mail_title(self, mail_title:str):
        self.message['Subject'] = Header(mail_title,'utf-8')

    def set_mail_content(self, mail_content:str):
        self.message.attach(MIMEText(mail_content, 'plain', 'utf-8'))

    def send_email(self):
        # 连接到SMTP服务器并发送邮件
        try:
            self.smtp = SMTP_SSL(self.smtp_server)                  # ssl登录
            self.smtp.login(self.smtp_username,self.smtp_password)
            self.smtp.sendmail(self.smtp_username,self.receiver,self.message.as_string())
            print('邮件发送成功')
        except Exception as e:
            print(f'邮件发送失败: {str(e)}')
        finally:
            self.smtp.quit()

    def send_text(self,text_file:str):
        """发送文本文件"""
        with open(text_file, 'rb') as file:
            attachment = MIMEText(file.read().decode('utf-8'))
            attachment.add_header('Content-Disposition', 'attachment', filename='example.txt')
            self.message.attach(attachment)

    def send_img(self,image_file:str):
        """发送图片"""
        with open(image_file, 'rb') as file:
            attachment = MIMEImage(file.read(), name='example.jpeg')
            attachment.add_header('Content-Disposition', 'attachment', filename='背景图.jpeg')
            self.message.attach(attachment)

    def send_application(self,file_path:str):
        """支持pdf,xlsx,mp3,mp4,zip等文件"""
        import os
        file_name = os.path.basename(file_path)
        with open(file_path, 'rb') as file:
            attachment = MIMEApplication(file.read(), name=file_name)
            attachment.add_header('Content-Disposition', 'attachment', filename=file_name)
            self.message.attach(attachment)




if __name__ == '__main__':

    # 请更改自己的邮箱号和授权码，以及接受者的邮箱列表,这里默认是使用qq邮箱发邮件，使用server是'smtp.qq.com' 
    user = 'your_email@qq.com'                               # 添加用户名
    pwd = 'xxxxxx'                                          # 授权码
    server = 'smtp.qq.com'  
    receiver = ['xxxxxx@qq.com','xxxx@qq.com']              # 接受者的邮箱列表
    
    # 以下都是作为附件发送的文件的本地的路径（可选）
    # 1.添加文本文件附件路径
    text_file = 'example/example.txt'
    # 2.添加图片附件路径
    image_file = 'example/example.jpeg'
    # 3.添加Excel附件路径
    excel_file = 'example/example.xlsx'
    # 4.添加压缩包附件路径
    zip_file = 'example/example.zip'
    # 5.添加PDF附件路径
    pdf_file = 'example/example.pdf'
    # 6.添加音频文件附件路径
    audio_file = 'example/example.mp3'  
    # 7.添加视频文件附件路径
    video_file = 'example/example.mp4'  

    server = Email(user,pwd,receiver)     # server默认'smtp.qq.com'
    server.set_mail_title('测试标题')      # 设置标题
    server.set_mail_content('测试内容')    # 设置邮件的文本内容
    server.send_img(image_file)           # (可选)
    server.send_text(text_file)           # (可选)
    server.send_application(excel_file)   # (可选)
    server.send_application(zip_file)     # (可选)
    server.send_application(pdf_file)     # (可选)
    server.send_application(audio_file)   # (可选)
    server.send_application(video_file)   # (可选)
    server.send_email() 