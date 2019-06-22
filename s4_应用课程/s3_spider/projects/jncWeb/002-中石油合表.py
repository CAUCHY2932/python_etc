# -*-coding:utf-8-*-
import os

filepath='./中石油'

fileHebing='./hebing4.csv'



def main():
    for item in os.listdir(filepath):


        with open('{filepath}/{item}'.format(filepath=filepath, item=item), 'r')as f:
            lst=f.readlines()

        with open(fileHebing,'a+') as f:
            f.write('{item}, \n'.format(item=item))
            for l in lst:
                f.write(l)


if __name__=="__main__":
    main()