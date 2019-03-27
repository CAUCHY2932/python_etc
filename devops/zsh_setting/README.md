# zsh setting

## zsh description

zsh is shell, which is very powerful,
I like the git hint, and clean tips.
## check you have zsh
```
cat /etc/shells
```
if you have not, I suggest you have a try

## install the zsh
### centos install
```
sudo yum -y install zsh

```
### ubuntu install
```
sudo apt-get -y install zsh
```

and you can check you have zsh when you have execute above



## change your default shell to zsh
```
chsh -s /bin/zsh
```
## install enhance setting - oh my zsh!
```
sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
```
## index back

if you have install miniconda or conda and so on (like some setting in ~/.bashrc), it can be not work, you should copy this setting to ~/.zshrc, and use the script
```
source ~/.zshrc
```

it can be work good!

