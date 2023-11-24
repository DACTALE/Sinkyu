import os

# 顔画像フォルダの絶対パスを取得
folder_name = "faces"
absolute_path = os.path.abspath(folder_name)

# 画像が保存されているフォルダのパス
folder_path = absolute_path

# フォルダ内のすべてのファイル名をリストに格納
file_names = os.listdir(folder_path)

# 画像ファイルのみ選択し、そのパスをリストに格納
img_files = [os.path.join(folder_path, f) for f in file_names if f.endswith('.png') or f.endswith('.jpg')]