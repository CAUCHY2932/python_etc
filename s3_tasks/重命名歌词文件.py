# coding:utf-8
import os
import shutil


def rename_lyric_file(target_file_path):

    # file_list = [x for x in os.listdir(target_file_path) if os.path.splitext(x)[1] == '.lrc']
    for item in os.listdir(target_file_path):
        pre, suffix = os.path.splitext(item)
        if suffix == '.lrc':
            new_filename = pre + ' - 俞敏洪' + '.lrcx'
            try:
                # os.rename(os.path.join(target_file_path, item), os.path.join(target_file_path, new_filename))
                shutil.copy(os.path.join(target_file_path, item), os.path.join(target_file_path, new_filename))
            except Exception as e:
                print('[error]-', e)
            else:
                print('[success]-have copy %s!'%new_filename)
    pass

if __name__ == "__main__":
    rename_lyric_file('/Users/young/Music/LyricsX')
    pass

