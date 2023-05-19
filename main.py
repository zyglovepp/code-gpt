import os
import chardet
import time

def merge_files(folder_path, output_file):
    """
    将文件夹中的所有代码文件内容合并到一个txt文件中
    :param folder_path: 文件夹路径
    :param output_file: 输出txt文件名
    :return: 写入文件数量
    """
    count = 0  #记录写入的文件数量
    # 测试能否写入文件权限
    try:
        with open(output_file, mode='w', encoding='utf-8') as f:
            pass
    except Exception as e:
        print(f"Error: {e}")
    # 如果文件不存在，则创建一个
    if not os.path.exists(output_file):
        open(output_file, 'w').close()
    # 增加写入权限
    os.chmod(output_file, 0o777)
    # 打开或新建txt文件
    with open(output_file, mode='w+', encoding='utf-8') as out_file:
        # 获取文件夹中的文件列表
        file_list = os.listdir(folder_path)
        # 按照名称排序
        file_list.sort()
        for f in file_list:
            # 获取文件路径
            file_path = os.path.join(folder_path, f)
            
            # 如果是文件夹，则递归处理
            if os.path.isdir(file_path):
                count += merge_files(file_path, output_file)
            # 如果是代码文件，则添加到txt中
            elif f.endswith('.py') or f.endswith('.cpp') or f.endswith('.c') or f.endswith('.java') or f.endswith('.json'):
                print(f"正在处理文件：{file_path}")
                # 获取文件名
                filename = os.path.splitext(f)[0]
                # 读取文件内容
                try:
                    with open(file_path, mode='r', encoding='utf-8') as code_file:
                        content = code_file.read()
                        # print(content)
                except UnicodeDecodeError as e:
                    encoding = chardet.detect(open(file_path, 'rb').read())['encoding'] # 获取文件编码方式
                    print(f"Error: {e}, skip {file_path}")
                    # 尝试使用文件编码方式再次读取文件
                    try:
                        with open(file_path, mode='r', encoding=encoding) as code_file:
                            content = code_file.read()
                            # 将*替换掉无法解析的中文
                            content = content.replace("\uFFFD", "*")
                            # print(content)
                    except Exception as e1:
                        print(f"Error: {e1}, skip {file_path}")
                        continue
                #缓冲
                out_file.flush()
                # 添加文件名和分隔符到txt中
                out_file.write(f"{filename}\n{'-'*50}\n")
                # 将代码添加到txt中
                content = content.replace('\t', ' ' * 4)  # 将制表符替换为四个空格
                # print(content)
                out_file.write(f"{content}\n\n")
                # 使用缓冲区和sleep保证所有内容能够写入文件
                os.fsync(out_file)  
                count += 1
                
        
        time.sleep(0.1)
    return count
   

if __name__ == '__main__':
    if os.getpid() == 0:
        print("当前程序以系统权限运行")
    else:
        print("当前程序未以系统权限运行")
    # 设置输入文件夹路径（注意使用原始字符串）
    folder_path = r'C:\CODE-File\ai\mj\midjourney-proxy'
    # 设置输出txt文件名
    output_file = 'output.txt'
    # 合并文件
    count = merge_files(folder_path, output_file)
    print(f"共写入 {count} 个文件。")
