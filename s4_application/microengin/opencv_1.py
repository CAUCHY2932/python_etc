# coding:utf-8


import cv2

file_name = 'testImg.png'
markLineWeight = 2
markLineColor = (255, 0, 0)

def main():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + \
        'haarcascade_frontalface_default.xml')
    img = cv2.imread(file_name)
