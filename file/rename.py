'''
Created on 2019年1月29日
@author:  Yvon_fajin
'''
import os ,os.path

def rename(file,keyword):
    ''' file: 文件路径    keyWord: 需要修改的文件中所包含的关键字 '''
    os.chdir(file)
    items = os.listdir(file)
    print(os.getcwd())
    for name in items :
        print(name)
        # 遍历所有文件
        if not os.path.isdir(name):
            if keyword in name :
                ''' 替换为空 '''
                new_name = name.replace(keyword,'')
                os.renames(name,new_name)
        else:
            rename(file + '\\' + name, keyword)
            os.chdir('...')
    print('-----------------------分界线------------------------')
    items = os.listdir(file)
    for name in items:
        print(name)

# rename('F:\java视频\中华石杉\互联网Java工程师面试突击 第二季', '互联网Java工程师面试突击 第二季')
rename('D:\\note\\尼恩\\Java面试红宝书V30（史上最全 + 持续更新）', '-from-Java面试红宝书-release')