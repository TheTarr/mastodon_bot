import base64
from Crypto.Cipher import AES

'''
采用AES对称加密算法
'''
# str不是16的倍数那就补足为16的倍数
def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes
#加密方法
def encrypt_oracle(mystr):
    # # 秘钥
    # key = '123456'
    # # 待加密文本
    # # mystr = '人生苦短，py是岸'
    # text = base64.b64encode(mystr.encode('utf-8')).decode('ascii')
    # # 初始化加密器
    # aes = AES.new(add_to_16(key), AES.MODE_ECB)
    # #先进行aes加密
    # encrypt_aes = aes.encrypt(add_to_16(text))
    # #用base64转成字符串形式
    # encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes
    mystr = mystr.encode('utf-8')
    encrypted_text = base64.b64encode(mystr)
    return encrypted_text
#解密方法
def decrypt_oralce(text):
    # # 秘钥
    # key = '123456'
    # # 密文
    # # text = 'ofyYz83X2RP0QeGYQH3JrU1rd7NLlN4LJSS9F6iOD/E='
    # # 初始化加密器
    # aes = AES.new(add_to_16(key), AES.MODE_ECB)
    # #优先逆向解密base64成bytes
    # base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
    # #
    # decrypted_text = str(aes.decrypt(base64_decrypted),encoding='utf-8') # 执行解密密并转码返回str
    # decrypted_text = base64.b64decode(decrypted_text.encode('utf-8')).decode('utf-8')
    decrypted_text = base64.b64decode(text)
    return decrypted_text

# if __name__ == '__main__':
#    value = encrypt_oracle("你好，世界")
#    print(decrypt_oralce(value))

def decode_poem(path):
    f = open(path, "r", encoding='UTF-8')   #设置文件对象
    for i in f.readlines():
        h = decrypt_oralce(i[2:])
        print(h.decode())
    f.close() #关闭文件

def encode_poem(path):
    f = open(path, "r", encoding='UTF-8')   #设置文件对象
    for i in f.readlines():
        h = encrypt_oracle(i)
        print(h)
    f.close() #关闭文件
