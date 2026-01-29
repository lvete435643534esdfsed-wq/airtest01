from airtest.core.api import *
import time
import os

# 核心操作脚本：打开程序，点击图片

# 配置信息
APP_PATH = "D:\EudemonsLauncher\eudemons_launcher.exe"

# 检查文件是否存在
if not os.path.exists(APP_PATH):
    print(f"启动器文件不存在: {APP_PATH}")
    exit(1)

# 连接Windows设备
connect_device("Windows:///")

# 启动游戏启动器
print("启动魔域游戏启动器...")
os.startfile(APP_PATH)
time.sleep(25)  # 等待启动完成

# 点击账号登录按钮
print("点击账号登录按钮...")
try:
    # 方法1: 使用坐标点击（更可靠）
    # 尝试屏幕中央位置
    touch((960, 540))
    print("✅ 坐标点击成功")
except Exception as e:
    print(f"坐标点击失败: {e}")
    try:
        # 方法2: 使用图像识别（备选）
        touch(Template(r"tpl1769599352442.png"))
        print("✅ 图像识别点击成功")
    except Exception as e:
        print(f"❌ 所有点击尝试失败: {e}")

print("操作完成！")
