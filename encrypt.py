import util
import sys


def encrypt():
    if len(sys.argv) <= 1:
        print("请输入要加密的文件路径")
        exit(-1)
    print("开始读取密钥文件")
    with open("aes_key.key", "r") as file:
        key = file.read().encode('utf-8')
    print("开始加密")
    with open(sys.argv[1], "rb") as file_src:
        if len(sys.argv) >= 3:
            des_path = sys.argv[2]
        else:
            des_path = sys.argv[1] + ".crypt"
        with open(des_path, "wb") as file_des:
            count = 0
            buf = file_src.read(util.block_size)
            while len(buf) != 0:
                buf = util.encrypt(buf, key)
                file_des.write(buf)
                count += util.block_size / (1024 * 1024)
                print("已完成 {} MB".format(count))
                buf = file_src.read(util.block_size)
    print("加密完成")
    return 0


if __name__ == '__main__':
    exit(encrypt())

