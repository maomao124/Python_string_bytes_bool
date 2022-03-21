"""
 * Project name(项目名称)：Python字符串_bytes_bool 
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/21 
 * Time(创建时间)： 18:18
 * Version(版本): 1.0
 * Description(描述)： bytes类型及用法
 """

if __name__ == '__main__':
    # 通过构造函数创建空 bytes
    b1 = bytes()
    # 通过空字符串创建空 bytes
    b2 = b''
    print(b1)
    print(b2)
    # 通过b前缀将字符串转换成 bytes
    b3 = b"hello"
    print(b3)
    print(b3[1])
    print(b3[2])
    print(b3[3])
    print(b3[1:4])
    # 为 bytes() 方法指定字符集
    b4 = bytes('hello', encoding='UTF-8')
    print(b4)
    # 通过 encode() 方法将字符串转换成 bytes
    b5 = "hello".encode('UTF-8')
    print(b5)
