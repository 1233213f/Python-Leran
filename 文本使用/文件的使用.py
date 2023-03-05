# 文件的使用
# 文本形式打开文件
tf = open("1.txt", "rt")
print(tf.readline())  # readline读取第一行-->中国是一个伟大的国家！
tf.close()

# 二进制形式打开文件
bf = open("1.txt", "rb")
print(
    bf.readline())  # readline读取第一行-->b'\xd6\xd0\xb9\xfa\xca\xc7\xd2\xbb\xb8\xf6\xce\xb0\xb4\xf3\xb5\xc4\xb9\xfa\xbc\xd2\xa3\xa1'
bf.close()

# 文件处理的步骤:打开-操作-关闭
# 打开模式
'''
'r':只读模式，如果文件不存在，返回FileNotFoundError
'w':覆盖写模式，文件不存在则创建，存在则完全覆盖
'x':创建写模式,文件不存在则创建，存在则返回
'a':追加写模式，文件不存在则创建，存在则在文件最后追加内容
'b':二进制文件模式
't':文本文件模式，默认值
'+':与/r/w/x/a配合使用，在原功能基础上增加同时读写功能
'''
tf = open("1.txt", "rt")
size = -1
print(tf.read(size))  # 读取指定内容长度的内容，如果不给size参数或size=-1则读入全部内容
print(tf.read(size))  # 注意，不能连续读2次，因为文件被占用了
tf.close()  # 先关闭后面才能读取
tf = open("1.txt", "rt")
print("readline方法")
print(tf.readline(0))  # size=-1或不给size参数，读入一行内容,size>=0读入该行size长度
tf.close()  # 先关闭后面才能读取

tf = open("1.txt", "rt")
print(tf.readlines(size))  # 读入文件所有行，以每行为元素形成列表,如给出size参数，则读取前size行
tf.close()  # 先关闭后面才能读取

# 遍历全文本之方法1
# 一次读入，统一处理
print("遍历全文本之方法1：一次读入，统一处理")
fo = open("1.txt", 'r')
txt = fo.read()
print(txt)
fo.close()

# 遍历全文本之方法2
# 按数量读入，逐步处理
print("遍历全文本之方法2：按数量读入，逐步处理")
fo = open("1.txt", 'r')
txt = fo.read(2)  # 读入2个长度的文本
while txt != "":
    print(txt)
    txt = fo.read(2)
fo.close()

# 遍历全文本之方法3
# 逐行遍历文件
print("遍历全文本之方法3：逐行遍历文件")
fo = open("1.txt", 'r')
txt = fo.readline()  # 读入一行
while txt != "":
    print(txt)
    txt = fo.readline()
fo.close()

# 遍历全文本之方法4
# 逐行遍历文件
print("遍历全文本之方法4：逐行遍历文件")
fo = open("1.txt", 'r')
for line in fo:
    print(line)
fo.close()

# 遍历全文本之方法5
# 逐行遍历文件
print("遍历全文本之方法5：逐行遍历文件")
fo = open("1.txt", 'r')
for line in fo.readlines():
    print(line)
fo.close()

# 数据的文件写入
fo = open("1.txt", "w+")
fo.write("\n此致敬礼")
print(fo.read())
fo.close()

fo = open("1.txt", "w+")
ls = ["中国", "法国", "美国"]
fo.writelines(ls)
print(fo.read())
fo.close()

# fo.seek(offset) 改变当前文件操作指针的位置
'''
offset定义：
0--文件开通
1--当前位置
2--文件结尾
'''
print("练习")
fo = open("1.txt", "w+")
ls = ["中国", "法国", "美国"]
fo.writelines(ls)
fo.seek(0)  # 移动到文件头或文件尾
for line in fo:
    print(line)  # 移动到文件头或文件尾才有输出
