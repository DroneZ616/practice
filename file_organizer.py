import os
import shutil

# 1. 设置你要整理的文件夹路径（改成你自己的桌面路径）
# 提示：在资源管理器地址栏复制路径，或者直接写绝对路径
TARGET_FOLDER0 = r"C:\Users\徐圣涛\Desktop"

# 2. 定义分类规则（扩展名 -> 目标文件夹名）
CATEGORIES = {
    "图片": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "文档": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".md"],
    "压缩包": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "程序": [".exe", ".msi", ".bat", ".cmd"],
    "音视频": [".mp4", ".avi", ".mkv", ".mp3", ".wav", ".flac"],
    "代码": [".py", ".js", ".html", ".css", ".java", ".cpp", ".json", ".xml"],
}

def organize_folder(folder_path):
    """
    整理指定文件夹里的所有文件
    """
    # 3. 遍历文件夹里的所有内容
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # 跳过文件夹（只整理文件，不整理里面的文件夹）
        if os.path.isdir(file_path):
            continue
        
        # 4. 获取文件扩展名（后缀）
        _, ext = os.path.splitext(filename)  # 比如 "cat.jpg" -> ("cat", ".jpg")
        ext = ext.lower()  # 统一转小写，防止 ".JPG" 被漏掉
        
        # 5. 判断这个扩展名属于哪个类别
        target_folder = "其他"  # 默认归类到“其他”
        for category, exts in CATEGORIES.items():
            if ext in exts:
                target_folder = category
                break
        
        # 6. 构建目标文件夹的完整路径，并创建它（如果不存在）
        target_path = os.path.join(folder_path, target_folder)
        os.makedirs(target_path, exist_ok=True)  # exist_ok=True 表示目录已存在也不报错
        
        # 7. 移动文件
        shutil.move(file_path, target_path)
        print(f"✅ 已移动：{filename} -> {target_folder}")
    
    print("\n🎉 整理完成！")

def judge():

    try:
        TARGET_FOLDER = 1
        confirm = input(
        """
        该操作会将文件夹内的所有文件按类型分类整理到子文件夹中，原有文件夹结构将被改变。
        确认开始整理文件？(A:yes/B:no): 
        """
        )
        if confirm.lower() == 'a':
            # 安全检查：让用户确认一下目标路径
            while True:
                TARGET_FOLDER = input(
                    f""""
请输入要整理的文件夹路径（默认：{TARGET_FOLDER0}）：
设置你要整理的文件夹路径
提示：在资源管理器地址栏复制路径，或者直接写绝对路径
"""
                    ) or TARGET_FOLDER0
                # 检查路径是否存在
                if not os.path.exists(TARGET_FOLDER):
                    print(f"❌ 路径不存在：{TARGET_FOLDER}")
                    print('请重新输入正确的路径')
                        
                elif not os.path.isdir(TARGET_FOLDER):
                    print(f"❌ 路径不是一个文件夹：{TARGET_FOLDER}")
                    print('请重新输入正确的路径')
                    
                else:
                    break  # 路径合法，跳出循环
            print(f"即将整理文件夹：{TARGET_FOLDER}")
            try:
                final_confirm = input(
                    f"""
当前路径：{TARGET_FOLDER}
确认继续？(A:yes/B:no):
"""
                )
                if final_confirm.lower() == 'a':
                    organize_folder(TARGET_FOLDER)
                elif final_confirm.lower() == 'b':
                    print("已取消。")
                else:
                    print('输入错误')
            except KeyboardInterrupt:
                print("\n用户中断操作，退出。")
                return
            except Exception as e:
                print(f"程序遇到意外错误：{e}")
                
                
        elif confirm.lower() == 'b':
            print("已取消。")
        else:
            print('输入错误')
    except KeyboardInterrupt:
        print("\n用户中断操作，退出。")
        return
    except Exception as e:
        print(f"程序遇到意外错误：{e}")

# 8. 程序入口（和 rps.py 一样，增加安全性）
if __name__ == "__main__":
    judge()
    

    
