# coding: utf-8
import os


# os.path.splittxt()
# os.listdir()
# os.getcwd()
# os.rename()


def changeSingle(fileName, suffixPre, suffixAfter):
    """
    fileName指的是文件名
    suffix指的是后缀名
    """
    partion = os.path.splitext(fileName)
    print(partion)

    if partion[1] == '.'+suffixPre:
        nameNew = partion[0]+'.'+suffixAfter


def changeFileName():
    files = os.listdir('')


def chk_permisson(path, mode):
    # 检验权限模式
    os.access(path, mode)


def chdir(path):
    # 改变当前工作目录
    os.chdir(path)


def chflags(path):
    # 设置路径的标记为数字标记
    os.chflags(path)


def chmod(path, mode):
    # 更改权限

    os.chmod(path, mode)


def chown(path, uid, gid):
    # 更改文件所有者
    os.chown(path, uid, gid)


def chroot(path):
    # 更改当前进程的根目录
    os.chroot(path)


def close(fd):
    # 关闭文件描述符
    os.close(fd)


def closerange(fd_low, fd_high):
    # 关闭所有文件描述符，从fd_low（包含）到fd_high（不包含），错误会忽略
    os.closerange(fd_low, fd_high)


def dup(fd):
    # 复制文件描述符fd
    os.dup(fd)


def du2(fd, fd2):
    # 将一个文件描述符fd复制到另一个fd2
    os.du2(fd, fd2)

def fchdir(fd):
    # 通过文件描述符改变当前工作目录
    os.fchdir(fd)


def fchmod(fd, mode):
    # 改变一个文件的访问权限，该文件由参数fd指定，参数mode是unix下的文件访问权限
    os.fchmod(fd, mode)


def fchown(fd, uid, gid):
    # 修改一个文件的所有权，这个函数修改一个文件的用户id和用户组id，该文件由文件描述符fd指定
    os.fchown(fd, uid, gid)


def fdatasync(fd):
    # 强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息
    os.fdatasync(fd)
