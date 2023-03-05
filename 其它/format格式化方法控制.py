# format格式化方法控制
a = "{:=^20}".format("PYTHON")
# 输出20个=，PYTHON在中间对齐
print(a)

a = "{0:*>20}".format("BIT")
# 右对齐输出20个*+BIT

print(a)
a = "{:10}".format("BIT")

print(a)
