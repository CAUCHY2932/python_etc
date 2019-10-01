import os


def clean_text(filename):
    # 有时候要指定utf-8，当遇到中文时
    with open(filename, mode='r', encoding='utf-8') as f:
        fr = f.readlines()
    fh = [x for x in fr if x.strip()!='']
    return fh


def test_strip():
    a = ' sdfds \n'
    if a.strip() == '':
        print('success')
    print(a)
    pass


def write_to_file(new_filename, content):
    # 当遇到中文时，必须指定utf-8
    with open(new_filename, mode='w', encoding='utf-8') as f:
        f.write(content)
        print('success!\n')
    

if __name__ == '__main__':
    # test_strip()
    filename = '管理学定律2.txt'
    new_filename = '管理学定律清洗后2.txt'
    fh = clean_text(filename)
    write_to_file(new_filename, ''.join(fh))
    pass
    