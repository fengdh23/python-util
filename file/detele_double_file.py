import os
from pathlib import Path

def remove_simple_duplicates(folder_path):
    folder = Path(folder_path)
    if not folder.is_dir():
        print(f"错误：路径不存在或不是文件夹 → {folder_path}")
        return

    # 获取所有文件名（用于快速查找）
    file_names = set(f.name for f in folder.iterdir() if f.is_file())

    to_delete = []

    for name in file_names:
        # 检查是否是 (1) 结尾的文件，例如 "a(1).mp3"
        if name.endswith('(1).mp3') or name.endswith('(1).MP3'):
            # 构造对应的原始文件名：把 "(1).mp3" 替换为 ".mp3"
            original_name = name.replace('(1).mp3', '.mp3').replace('(1).MP3', '.MP3')
            if original_name in file_names:
                to_delete.append(folder / name)

    if not to_delete:
        print("未发现符合规则的重复文件。")
        return

    print("将删除以下重复文件（因存在对应的原始文件）：")
    for f in to_delete:
        print(f"  - {f.name}")

    confirm = input(f"\n共 {len(to_delete)} 个文件。确认删除？(y/N): ")
    if confirm.lower() == 'y':
        for f in to_delete:
            try:
                f.unlink()
                print(f"✅ 已删除: {f.name}")
            except Exception as e:
                print(f"❌ 删除失败 {f.name}: {e}")
    else:
        print("操作已取消。")

# ===== 使用 =====
if __name__ == "__main__":
    path = input("请输入歌曲文件夹路径: ").strip().strip('"')
    remove_simple_duplicates(path)