def main():
    fileName =input ("What file are the numbers in?")
    infile =open(fileName ,'r',encoding='utf-8')
    sum=0.0
    count=0
    line =infile.readline()
    while line !="":#外循环：while语句对每行循环一次
    #为line中的值更新其count和sum
        for xStr in line.split(","):#内循环：for语句对一行中每个数字进行循环
            sum=sum+eval(xStr)
            count=count+1
        line=infile.readline()
    print("\nThe average of the numbers is",sum/count)
main()
#在运行代码时必须将文件的路径以及文件的名称，还有文件的后缀输入
#例：C:\Users\28590\Desktop\1.txt
#适合每行行以逗号隔开的数字  例如：
#2,2,3,45,6,7
#44,45,24,345,535,7
#,encoding='utf-8'
