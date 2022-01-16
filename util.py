from Crypto.Cipher import AES
from Crypto import Random

block_size = 1024 * 1024 * 512
head_size = 17


# 如果text不足16位的倍数就用空格补足为16位
def add_to_16(text):
    if len(text) % 16:
        add = 16 - (len(text) % 16)
    else:
        add = 0
    text = text + ('\0'.encode('utf-8') * add)
    return text, add


# 加密函数
def encrypt(text, key):
    mode = AES.MODE_CBC
    iv = Random.new().read(AES.block_size)
    text, add = add_to_16(text)
    cryptos = AES.new(key, mode, iv)
    text = cryptos.encrypt(text)
    text = hex(add)[2:].encode('utf-8') + iv + text
    # 因为AES加密后的字符串不一定是ascii字符集的，输出保存可能存在问题，所以这里转为16进制字符串
    return text


# 解密后，去掉补足的空格用strip() 去掉
def decrypt(text, key):
    add = int(text[0: 1].decode('utf-8'), 16)
    iv = text[1: 17]
    text = text[17:]
    mode = AES.MODE_CBC
    cryptos = AES.new(key, mode, iv)
    text = cryptos.decrypt(text)
    if add == 0:
        return text
    else:
        return text[:-add]


