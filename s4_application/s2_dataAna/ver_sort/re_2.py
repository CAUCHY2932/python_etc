import random


def find_max_ver(file_path):
    # 读取所有记录
    with open(file_path, 'r') as f:
        # lines = f.readlines()
        # print(type(lines))
        lines = [x.strip() for x in f.readlines()]

    # 设定第一行为最大版本号，最大版本号
    with open(file_path, 'r') as f:
        first_line = f.readline().strip()
        # max_version_header = first_line.split('.')[0]
    max_version_num = first_line
    print(max_version_num)

    for line in lines:
        current_line_list = line.split('.')
        max_version_num_list = max_version_num.split('.')
        print(current_line_list)
        print(max_version_num_list)
        print('-'*10)

        if len(current_line_list) < len(max_version_num_list):
            if line not in max_version_num:
                for item in zip(current_line_list, max_version_num_list):
                    if item[1] < item[0]:
                        max_version_num = line
                        break
                    elif item[1] > item[0]:
                        break
                    else:
                        pass
            else:
                pass
        elif len(current_line_list) > len(max_version_num_list):
            if max_version_num not in line:
                for item in zip(current_line_list, max_version_num_list):
                    if item[1] < item[0]:
                        max_version_num = line
                        break
                    elif item[1] > item[0]:
                        break
                    else:
                        pass
            else:
                max_version_num = line
        else:
            for item in zip(current_line_list, max_version_num_list):
                if item[1] < item[0]:
                    max_version_num = line
                    break
                elif item[1] > item[0]:
                    break
                else:
                    pass

            pass

    return max_version_num


def gen_random_ver(num):
    for _ in range(num):
        # print(random.randint(1, 50))
        ver_num = '{}.{}.{}'.format(random.randint(1, 20),
                                    random.randint(0, 20),
                                    random.randint(0, 20))
        yield ver_num


def write_random_ver(file_path='./1234.txt'):
    ver_nums = '\n'.join([x for x in gen_random_ver(100)])

    with open(file_path, 'w') as f:
        f.write(ver_nums)


if __name__ == "__main__":
    ret = find_max_ver('./1234.txt')
    print(ret)
