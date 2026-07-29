import os

def rename_folder():
    new_name=input("请输入新文件夹名称：")

    folder_path0 = r"C:\Users\徐圣涛\Desktop\空文件夹"
    folder_path1 = r"C:\Users\徐圣涛\Desktop\\" + new_name

    if os.path.exists(folder_path0) :
        os.replace(folder_path0, folder_path1)
        print(f"已重命名{os.path.basename(folder_path1)}")

    if os.path.exists(folder_path1) :
        print(f"已存在{os.path.basename(folder_path1)}")

    else:
        print("文件夹不存在")
        print('重新创建文件')
        os.makedirs(folder_path1)
        print(f"已创建{os.path.basename(folder_path1)}")
        folder_path0 = folder_path1
if __name__ == '__main__':
    rename_folder()

