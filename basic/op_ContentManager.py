# f = open("file\\test.txt", "r", encoding="utf-8")
# f.write('welcome')
# f.write('to')
# f.write('python')
# f.close()
#
#
# with open("file\\test.txt", "r", encoding="utf-8") as fo:
#     fo.write("welcome to python")



class MyFileOpen:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.fo = None

    def __enter__(self):
        self.fo = open(self.filename, self.mode, encoding="utf-8")
        return self.fo

    def __exit__(self, *unused_args):
        self.fo.close()

# 使用
with MyFileOpen("test.txt", "w") as fo:
    fo.write("welcome to python")
    fo.write('大海你太牛掰了')
    print("文件已关闭")
