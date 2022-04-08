# -*- coding: UTF-8 -*-
import os

def convert(dir):
    file_list = os.listdir(dir)
    n=0
    print(file_list)
    for filename in file_list:
        oldname=dir+file_list[n]

    #设置新文件名
    s=str(n+1)
    st=s.zfill(1)
    newname=dir+s+'.jpg'

    #用os模块中的rename方法对文件改名
    os.chdir(dir)
    os.rename(oldname,newname)
    print(oldname,'====》',newname)

    n+=1

if __name__ == '__main__':
   dir = raw_input('C:\\Users\\Administrator\\Desktop\\图片库1')
   convert(dir)