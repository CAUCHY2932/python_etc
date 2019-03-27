# 发送邮件demo

__author__ = 'young'

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
