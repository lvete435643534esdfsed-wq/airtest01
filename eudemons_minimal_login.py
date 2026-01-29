from airtest.core.api import *
import time
import os

print("魔域游戏启动器登录测试脚本（极简版）")
print("=" * 60)

# 配置信息
APP_PATH = "D:\EudemonsLauncher\eudemons_launcher.exe"  # 魔域游戏启动器路径

# 检查文件是否存在
if not os.path.exists(APP_PATH):
    print(f"❌ 启动器文件不存在: {APP_PATH}")
    exit(1)

print(f"启动器路径: {APP_PATH}")

# 连接Windows设备
print("连接Windows设备...")
try:
    connect_device("Windows:///")
    print("✅ Windows设备连接成功")
except Exception as e:
    print(f"❌ Windows设备连接失败: {e}")
    exit(1)

time.sleep(2)

# 启动游戏启动器
print(f"启动魔域游戏启动器...")
try:
    # 使用os.startfile来启动应用，更可靠
    os.startfile(APP_PATH)
    print("✅ 启动器启动成功")
except Exception as e:
    print(f"❌ 启动器启动失败: {e}")
    exit(1)

time.sleep(20)  # 等待启动器完全启动

# 直接使用坐标点击
print("执行账号登录操作...")
try:
    # 简单的坐标点击，假设游戏窗口在屏幕中央
    # 注意：这里的坐标需要根据实际情况调整
    # 建议使用AirtestIDE的截图功能获取准确坐标
    
    # 点击屏幕中央位置
    # 对于大多数应用，登录按钮通常在窗口中央或下方
    touch((960, 540))  # 假设屏幕分辨率为1920x1080
    print("✅ 执行点击操作成功")
    
    # 等待登录界面出现
    time.sleep(5)
    print("✅ 脚本执行完成")
    
    print("\n使用建议：")
    print("1. 建议使用AirtestIDE打开此脚本")
    print("2. 在AirtestIDE中启动游戏启动器")
    print("3. 使用AirtestIDE的截图功能捕获账号登录按钮")
    print("4. 将脚本中的坐标点击替换为图像识别点击")
    print("\n例如：")
    print("touch(Template('login_button.png'))")
    
except Exception as e:
    print(f"❌ 操作失败: {e}")

print("\n测试脚本执行完成！")
print("=" * 60)
