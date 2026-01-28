from airtest.core.api import *
import time
import os

print("魔域游戏启动器登录测试脚本（最终版）")
print("=" * 60)

# 配置信息
APP_PATH = "D:\EudemonsLauncher\eudemons_launcher.exe"  # 魔域游戏启动器路径

# 检查文件是否存在
if not os.path.exists(APP_PATH):
    print(f"❌ 启动器文件不存在: {APP_PATH}")
    exit(1)

print(f"启动器路径: {APP_PATH}")

# 步骤0: 连接Windows设备
print("步骤0: 连接Windows设备")
try:
    connect_device("Windows:///")
    print("✅ Windows设备连接成功")
except Exception as e:
    print(f"⚠️  Windows设备连接失败: {e}")
    print("继续执行，尝试其他方式")

# 步骤1: 启动游戏启动器
print("\n步骤1: 启动魔域游戏启动器")
try:
    # 使用os.startfile来启动应用，最可靠的方式
    os.startfile(APP_PATH)
    print("✅ 启动器启动成功")
except Exception as e:
    print(f"❌ 启动器启动失败: {e}")
    exit(1)

# 等待启动器完全启动
print("等待启动器启动完成...")
time.sleep(25)  # 给足够的时间让启动器加载
print("✅ 启动器启动完成")

# 步骤2: 执行登录操作
print("\n步骤2: 执行登录操作")
print("提示: 此脚本使用坐标点击方式")
print("建议：在实际使用时，使用AirtestIDE的截图功能")
print("捕获账号登录按钮的图片，然后使用图像识别点击")

# 尝试点击屏幕中央位置
try:
    # 假设游戏窗口在屏幕中央
    # 这里的坐标需要根据实际屏幕分辨率调整
    # 对于1920x1080的屏幕，中央位置是(960, 540)
    # 对于1366x768的屏幕，中央位置是(683, 384)
    
    # 尝试多个可能的位置
    possible_positions = [
        (960, 540),   # 1920x1080屏幕中央
        (683, 384),   # 1366x768屏幕中央
        (800, 450),   # 1600x900屏幕中央
        (1024, 576),  # 2048x1152屏幕中央
    ]
    
    print("尝试点击可能的账号登录按钮位置...")
    
    for i, pos in enumerate(possible_positions):
        print(f"尝试位置 {i+1}: {pos}")
        try:
            touch(pos)
            print(f"✅ 点击位置 {pos} 成功")
            # 每次点击后等待2秒
            time.sleep(2)
        except Exception as e:
            print(f"❌ 点击位置 {pos} 失败: {e}")
    
    print("\n✅ 登录操作执行完成")
except Exception as e:
    print(f"❌ 登录操作失败: {e}")

# 步骤3: 验证结果
print("\n步骤3: 验证结果")
print("⚠️  由于没有图像识别，无法自动验证登录是否成功")
print("请手动检查游戏启动器是否进入登录界面")

print("\n测试脚本执行完成！")
print("=" * 60)
print("\n使用AirtestIDE优化脚本的步骤：")
print("1. 打开AirtestIDE")
print("2. 点击'打开脚本'，选择此文件")
print("3. 运行脚本启动游戏启动器")
print("4. 在AirtestIDE的设备窗口中，找到账号登录按钮")
print("5. 点击'截图'按钮捕获账号登录按钮")
print("6. 在脚本编辑区，将坐标点击替换为图像识别点击:")
print("   touch(Template('login_button.png'))")
print("7. 保存并重新运行脚本")
