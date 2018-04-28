# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

import smtplib
from email.mime.text import MIMEText

server_host = 'smtp.163.com'
username = '1903@163.com'
password = '08080808'


def send(to_mail):
    '''
    :param me: 发件人名称和邮箱账户
    :param to_list: 收件人邮箱
    :param sub: 邮件标题
    :param content: 内容
    '''
    me = "irobotbox" + "<" + username + ">"
    to_list = ['8022761@qq.com', to_mail]
    sub = "赛盒科技-阿里巴巴店铺名称抓取任务完成"
    content = "<h1>请点击下面的下载按钮进行下载当前任务的抓取结果</h1><a href='http://www.baidu.com'>下载文件</a>"

    # _subtype 可以设为html,默认是plain
    msg = MIMEText(content, _subtype='html')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ';'.join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(server_host)
        server.login(username, password)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
    except Exception as e:
        print(str(e))


def sendMailFile(filename, to_mail):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.application import MIMEApplication

    username = '1903@163.com'
    password = '08080808'
    sender = username
    receivers = ','.join([to_mail])

    # 如名字所示： Multipart就是多个部分
    msg = MIMEMultipart()
    msg['Subject'] = '赛盒科技-阿里巴巴店铺名称抓取任务抓取结果'
    msg['From'] = sender
    msg['To'] = receivers

    # 下面是文字部分，也就是纯文本
    puretext = MIMEText('您上传的任务已完成...')
    msg.attach(puretext)

    # 下面是附件部分 ，这里分为了好几个类型

    # 首先是xlsx类型的附件
    xlsxpart = MIMEApplication(open(filename, 'rb').read())
    xlsxpart.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(xlsxpart)

    # # jpg类型的附件
    # jpgpart = MIMEApplication(open('beauty.jpg', 'rb').read())
    # jpgpart.add_header('Content-Disposition', 'attachment', filename='beauty.jpg')
    # msg.attach(jpgpart)
    #
    # # mp3类型的附件
    # mp3part = MIMEApplication(open('kenny.mp3', 'rb').read())
    # mp3part.add_header('Content-Disposition', 'attachment', filename='benny.mp3')
    # msg.attach(mp3part)

    ##  下面开始真正的发送邮件了
    try:
        client = smtplib.SMTP()
        client.connect('smtp.163.com')
        client.login(username, password)
        client.sendmail(sender, receivers, msg.as_string())
        client.quit()
        print('带有附件的邮件发送成功！')
    except smtplib.SMTPRecipientsRefused:
        print('Recipient refused')
    except smtplib.SMTPAuthenticationError:
        print('Auth error')
    except smtplib.SMTPSenderRefused:
        print('Sender refused')
    except smtplib.SMTPException as e:
        print(e)

