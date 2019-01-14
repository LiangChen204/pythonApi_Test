#!//usr/local/bin python
# -*- coding:utf-8 -*-

# if __name__ == '__main__'的意思是：
# 当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；
# 当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行
if __name__ == "__mainn__":
    print("作为主程序运行")
else:
    print("package_runoob初始化")