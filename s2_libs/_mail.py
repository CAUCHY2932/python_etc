# coding:utf-8
import yagmail


class MailSender(object):
    def __init__(self, user: str, password: str, host: str, port: str) -> None:
        # self.user = user
        # self.password = password
        # self.host = host
        # self.port = port
        self.yag = yagmail.SMTP(user=user, password=password,
                                host=host, port=port)
        self.subject = ''
        self.attachment = None
        self.contents = None

    def send(self, obj_users: list, subject: str, attachments: list, contents: str) -> None:
        """发送邮件
        :param obj_users: 目标用户可为多个，如果为单个用户，我们可以像这样['hello@qq.com']
        :param subject: '这是一个邮件的主题'
        :param attachments: 附件，列表
        :param contents: 邮件内容
        :return: None
        """
        self.yag.send(obj_users, subject=subject, attachments=attachments, contents=contents)


def send_1():
    # EXAMPLE:
    # 这里的密码是授权码
    # python2需要在中文字符前加“u”，表示是Unicode编码
    USER = ''
    PASSWORD = ''
    HOST = 'smtp.qq.com'
    PORT = '465'
    SUBJECT = u'主题'
    ATTACHMENTS = [u'陈芳语 - 爱你.mp3', '002.md', '001.txt', '003.jpg']  # 传入附件的路径
    CONTENTS = '你好啊，这是正文'  # 正文
    # 以上为配置项

    obj_users = ['2932045582@qq.com']  # 目标用户的邮件地址,多用户接收邮件时为一个列表
    yag = yagmail.SMTP(user=USER, password=PASSWORD, host=HOST, port=PORT)
    # 单用户发送邮件
    yag.send(obj_users, subject=SUBJECT, attachments=ATTACHMENTS, contents=CONTENTS)


def send2():
    # # EXAMPLE:
    # USER='2932045582@qq.com'
    # PASSWORD=''
    # HOST='smtp.qq.com'
    # PORT='465'
    # SUBJECT='主题'
    # ATTACHMENTS=[] # 传入附件的路径
    # CONTENTS='你好啊，这是正文'
    #
    # obj_users=[] # 目标用户的邮件地址,多用户接收邮件时为一个列表
    # yag = yagmail.SMTP(user=USER, password=PASSWORD, host=HOST, port=PORT)
    #
    # # 单用户发送邮件
    # yag.send(obj_users, subject = SUBJECT, attachments=ATTACHMENTS, contents=CONTENTS)
    #
    # # 向多用户发送邮件
    # yag.send()

    pass


def send_3():
    # # CONFIGS
    # USER=''
    # PASSWORD=''
    # HOST=''
    # PORT=''
    # SUBJECT=''
    # ATTACHMENTS=['','']
    #
    #
    # yag = yagmail.SMTP(user=USER, password=PASSWORD, host=HOST, port=PORT)
    # yag.send(USER, subject = SUBJECT, attachments=ATTACHMENTS)

    # # EXAMPLE:
    # USER='2932045582@qq.com'
    # PASSWORD=''
    # HOST='smtp.qq.com'
    # PORT='465'
    # SUBJECT='主题'
    # ATTACHMENTS=[] # 传入附件的路径
    # CONTENTS='你好啊，这是正文'
    #
    # obj_users=[] # 目标用户的邮件地址,多用户接收邮件时为一个列表
    # yag = yagmail.SMTP(user=USER, password=PASSWORD, host=HOST, port=PORT)
    #
    # # 单用户发送邮件
    # yag.send(obj_users, subject = SUBJECT, attachments=ATTACHMENTS, contents=CONTENTS)
    #
    # # 向多用户发送邮件
    # yag.send()

    pass
