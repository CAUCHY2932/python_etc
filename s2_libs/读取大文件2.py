# coding:utf-8

def read_chunks(file_obj, chunk_size=4096):
    while True:
        data = file_obj.read(chunk_size)
        if not data:
            break
        yield data


file_name = ''
f = open(file_name, 'r')
for chunk in read_chunks(f):
    pass
f.close()
