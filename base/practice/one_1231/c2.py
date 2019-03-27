origin=0

def go(step):
    new_pos=origin+step
    # origin=new_pos
    return origin
# 如果不重新赋值给外部变量，会被认为是闭包，否则会认为是局部变量，而局部变量是需要初始化的
# 如果变量出现在等号又被
print(go(6))
print(go(4))
print(go(9))
