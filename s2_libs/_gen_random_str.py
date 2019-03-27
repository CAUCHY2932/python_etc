import secrets


def gen_random_hex_string(digit_num):
    s_demo = secrets.token_hex(digit_num)
    return s_demo


if __name__ == '__main__':
    s = gen_random_hex_string(16)
    print(s)
