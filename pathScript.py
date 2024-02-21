import os

# 定义一个函数，用于查找指定目录及其子目录中的所有HTML文件
def find_html_files(root_dir):
    html_files = []  # 存储找到的HTML文件的相对路径
    for root, dirs, files in os.walk(root_dir):  # 遍历目录树
        for file in files:  # 遍历当前目录中的文件
            if file.endswith('.html'):  # 如果文件以'.html'结尾，则为HTML文件
                # 将HTML文件的路径转换为相对于根目录的路径，并将其添加到列表中
                html_files.append(os.path.relpath(os.path.join(root, file), root_dir))
    return html_files  # 返回HTML文件的相对路径列表

if __name__ == "__main__":
    root_dir = os.path.dirname(os.path.abspath(__file__))  # 获取脚本所在文件夹的绝对路径
    html_files = find_html_files(root_dir)  # 调用函数查找HTML文件
    print("HTML files relative paths:")  # 打印提示信息
    for html_file in html_files:  # 遍历HTML文件的相对路径列表
        print(html_file)  # 打印每个HTML文件的相对路径
