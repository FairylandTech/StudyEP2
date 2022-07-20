# 使用例子

```gitignore
# 注释内容: 忽略所有a.o文件
a.o
# 忽略从当前目录开始的a目录下的d.txt文件
/a/d.txt
# 忽略所有后缀为.a的文件
*.a
# 忽略所有后缀为.d或者.o的文件
*.[do]
# 忽略从根目录开始的文件夹c下的文件夹d
/c/d/
# 忽略所有的build文件夹
build/

# 所有的a.cfg文件都不忽略
!a.cfg
# 
# 所有的后缀为.out的文件都不忽略
!*.out

# 忽略build文件夹但是保留其中的a.txt文件
/build/
!/build/a.txt
# 忽略从当前文件夹开始的doc文件夹下和其子文件夹下所有文件后缀为 .pdf 的文件
doc/**/*.pdf
```
