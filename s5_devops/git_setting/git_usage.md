# git push usage

```
git remote add origin gitee.com/...
git remote add mirror github.com/...
gitpush() {
git push origin "$1"
git push mirror "$1"
}

usage: gitpush master

```



## command of usual

### git add -A
跟踪所有文件

### git commit -m "add some file"
提交并添加备注

### git remote -v 
查看远程分支

### git push mirror/origin master/dev

推送到远程分支

## 经常使用的组合
### 配置好本地和github、gitee的秘钥
### 在github新建一个仓库，初始化，并在gitee导入该仓库
### 在进行如下操作
#### git clone git@giteexxx
使用gitee克隆，速度较快
#### git remote add mirror git@githubxxx
添加远程分支

#### git push origin master
推送到远程分支,gitee
#### git push mirror master
推送到远程分支，github


