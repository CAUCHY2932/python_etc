# -*- coding:utf-8 -*-
"""
    create by young on 2019/1/2 14:29
"""
import yagmail

__author__ = 'young'

# EXAMPLE:
# 这里的密码是授权码
# python2需要在中文字符前加“u”，表示是Unicode编码
USER=''
PASSWORD=''
HOST='smtp.qq.com'
PORT='465'
SUBJECT=u'主题'
ATTACHMENTS=[u'陈芳语 - 爱你.mp3','002.md','001.txt','003.jpg'] # 传入附件的路径
CONTENTS='你好啊，这是正文' # 正文
# 以上为配置项




obj_users=['2932045582@qq.com'] # 目标用户的邮件地址,多用户接收邮件时为一个列表
yag = yagmail.SMTP(user=USER, password=PASSWORD, host=HOST, port=PORT)
# 单用户发送邮件
yag.send(obj_users, subject = SUBJECT, attachments=ATTACHMENTS, contents=CONTENTS)

