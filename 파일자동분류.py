import os
import shutil

# 다운로드 폴더 경로
download_folder = os.path.join("C:\\", "Users", "user", "Downloads")

# 이동할 폴더들
folders = {
    "images": os.path.join(download_folder, "images"),
    "data": os.path.join(download_folder, "data"),
    "docs": os.path.join(download_folder, "docs"),
    "archive": os.path.join(download_folder, "archive")
}

# 폴더 생성
for folder_path in folders.values():
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# 파일 확장자에 따라 이동
for filename in os.listdir(download_folder):
    file_path = os.path.join(download_folder, filename)
    if os.path.isfile(file_path):
        ext = filename.split(".")[-1]
        if ext.lower() in ["jpg", "jpeg"]:
            shutil.move(file_path, folders["images"])
        elif ext.lower() in ["csv", "xlsx"]:
            shutil.move(file_path, folders["data"])
        elif ext.lower() in ["txt", "doc", "pdf"]:
            shutil.move(file_path, folders["docs"])
        elif ext.lower() == "zip":
            shutil.move(file_path, folders["archive"])
