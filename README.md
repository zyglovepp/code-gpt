# code-gpt
当我们想要阅读一个项目代码文件的时候，往往只有readme.md里面的对整个项目的整体介绍，而不知道如何对代码文件间的逻辑理解，如果代码作者没有很好的标注代码注释，理解起来更是痛苦。当chatgpt出现的时候，我们发现能够用chatgpt帮助我们理解代码，但是面临一个问题就是我们要面对的不是一个代码文件，而是很多个文件夹嵌套文件。不过chatpdf的出现给了我一个启发：能不能将所有的文件全部转成一个pdf文件，这样就能通过chatpdf帮助我们理解代码间的逻辑。

主要实现思路：通过将整个项目的代码转成一个pdf格式文件，通过chatpdf帮助我们更好的理解代码。


# 实现过程
1. 通过main.py函数将整个代码文件夹转成txt文件，并且使用文件名+分隔符分割。
2. 使用https://convertio.co/zh/txt-pdf/ 网站将生成的txt文件转成pdf文件
3. 在https://www.chatpdf.com/ 网站使用ai分析整个项目

# 展示效果
## 先看看它对于某个代码文件的理解
![ScreenClip](https://github.com/zyglovepp/code-gpt/assets/70431495/84f86004-79bd-4438-8729-87dc91966457)
还可以，没有找错文件，也理解了这个文件的作用

## 接着看看它对于代码文件间的联系的理解
![ScreenClip](https://github.com/zyglovepp/code-gpt/assets/70431495/643f8ae2-aab7-42d9-960e-b2f4abfa1469)
好像也还不错，不过看到了其中提到了一些无关的信息。而且没有能够将该文件处于哪个文件夹下说出来（其实是因为我的main.py实现的功能问题，没有将文件夹名称加上，希望有大佬能够优化一下，感谢）

## 测试一下它会不会胡编乱造一些文件中没有提到的内容
![ScreenClip](https://github.com/zyglovepp/code-gpt/assets/70431495/c565c04a-23c2-43a1-8b1d-dba2d43854fc)
表现的还是不错的，能提醒我哪里理解错误

## 测试一下它能不能找到某个功能的实现代码
![ScreenClip](https://github.com/zyglovepp/code-gpt/assets/70431495/905433c4-8d20-4cef-a17f-972f291cc5ab)
可以的，表现不错

！！！ 最后强调！！！ chatpdf给出的答案并非真理，请结合具体代码分析，如果想要更加深入的修改或者注释，就复制相应的代码到chatgpt。chatpdf只是帮助我们更好更快的理解整个项目的逻辑。而且由于我自己的水平有限，没有很好的表现各个文件间相对路径的逻辑，如果有大佬有好的实现能够提交修改就更好了！感谢。

# 安装
直接复制或者使用 git clone 将代码复制到本地

# 运行
1. 修改需要读取的文件绝对路径：folder_path = r'你的文件绝对路径'
2. 然后运行main.py 
3. 得到输出的txt文件：out_file.txt
4. 然后使用https://convertio.co/zh/txt-pdf/ 网站将生成的txt文件转成pdf文件
5. 在https://www.chatpdf.com/ 网站使用chatpdf分析整个项目
