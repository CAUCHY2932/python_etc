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
