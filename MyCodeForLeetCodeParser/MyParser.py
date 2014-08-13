__author__ = 't-yaxue'
import os
import time

PATH = 'C:/Users/t-yaxue/Desktop/test'


def rename(fileItem):
    t = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    curName = fileItem.replace(' ', '-')
    curName = t + '-' + curName
    os.rename(PATH + '/' + fileItem, PATH + '/' + curName)
    print fileItem + "=>" + curName

def modify(fileItem):
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    header = "---\nlayout: post\ntitle: " + fileItem[:-3] + "\ndate: " + t + "\ndisqus: y\n---\n"
    headerCpp = "\n{% highlight c++ %}\n"
    headerpython = "\n{% highlight python %}\n"
    ender = "\n {% endhighlight %}\n"
    input = open(PATH + '/' + fileItem)
    lines = input.readlines()
    input.close()
    output = open(PATH + '/' + fileItem, 'w')
    output.write(header)
    flag = False
    for line in lines:
        if not flag:
            flag = True
            continue
        if "### C++:" in line:
            output.write(line)
            output.write(headerCpp)
        elif "### python:" in line:
            output.write(ender)
            output.write(line)
            output.write(headerpython)
        else:
            output.write(line)
    output.write(ender)
    output.close()
    print header

def main():

    fileList = os.listdir(PATH)
    for fileItem in fileList:
        modify(fileItem)
        rename(fileItem)

if __name__ == '__main__':
    main()