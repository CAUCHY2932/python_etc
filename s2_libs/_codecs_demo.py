# coding: utf-8
import chardet
import codecs

def coding_convert(filename):
    with open(filename, mode='rb') as f:
        frb = f.read()
    coding_detect = chardet.detect(frb)
    print(coding_detect)
    print(type(coding_detect))
    f_content = frb.decode(coding_detect.get('encoding'))
    print(f_content)


if __name__ == "__main__":
    coding_convert('批量插入.py')
