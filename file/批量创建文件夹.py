# -*- coding: UTF-8 -*-
import os

# 根文件夹
path = r'D:\\mknote\\'
# 文件夹，目前一级
name = [
    '企业应用',
    '技术新闻',
    '技术管理',
    '技术读物',
    '操作系统',
    "数据库",
    "杂项资源",
    "流程方法",
    "程序设计",
    "系统架构",
    "编程工具",
    "编程语言",
    "网络安全",
    "职场生涯",
    "趣味问题",
    "轶事趣闻"
]
for i in name:
    file_name = str(i)
    dir_name = path + file_name
    if file_name not in os.listdir(path):  # 文件夹名称不存在才创建
        os.mkdir(dir_name)
