import requests
import yagmail

# 若离消息通知类
class RlMessage:
    # 初始化类
    def __init__(self, mail,send_mail,password,host):
        self.mail = mail
        self.send_mail = send_mail
        self.password = password
        self.host = host

        
    def sendMail(self, status, msg):
        if self.mail == '':
            return '邮箱为空，已取消发送邮件！'
        to = self.mail
        user=self.send_mail
        password=self.password
        host=self.host
        print(to,user,password,host)
        yag = yagmail.SMTP(user=user, password=password, host=host)
        yag.send(to=to,subject=f'[{status}]今日校园通知',contents=msg)
        # try:
        #     yag = yagmail.SMTP(user=user, password=password, host=host)
        #     yag.send(to=to,subject=f'[{status}]今日校园通知',contents=msg)
        #     return '发送邮件成功！'
        # except Exception as e:
        #     print(e)
        #     return '发送邮件失败！'