def main():
    fileName =input ("What file are the numbers in?")
    infile =open(fileName ,'r')
    sum=0
    count=0
    for line in infile :
        sum=sum+eval(line)
        count=count+1
    print("\nThe average of the numbers is",sum/count)
main()
#在运行代码时必须将文件的路径以及文件的名称，还有文件的后缀输入
#例：C:\Users\28590\Desktop\1.txt
#适合一行一个数字
