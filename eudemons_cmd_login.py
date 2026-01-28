# -*- coding: utf-8 -*-
"""
魔域游戏启动器登录测试脚本（CMD兼容版）
专为在cmd命令提示符中执行而优化
"""

import sys
import os

# 确保编码正确
if sys.version_info[0] == 3:
    # Python 3
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("魔域游戏启动器登录测试脚本（CMD兼容版）")
print("=" * 60)

# 配置信息
APP_PATH = "D:\\EudemonsLauncher\\eudemons_launcher.exe"  # 使用双反斜杠，确保CMD兼容

# 检查文件是否存在
if not os.path.exists(APP_PATH):
    print(f"❌ 启动器文件不存在: {APP_PATH}")
    print("请检查路径是否正确，注意使用双反斜杠\\")
    sys.exit(1)

print(f"启动器路径: {APP_PATH}")
print(f"当前工作目录: {os.getcwd()}")

# 步骤0: 连接Windows设备
print("\n步骤0: 连接Windows设备")
try:
    from airtest.core.api import *
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
    print("请检查文件路径是否正确")
    sys.exit(1)

# 等待启动器完全启动
print("等待启动器启动完成...")
import time
time.sleep(25)  # 给足够的时间让启动器加载
print("✅ 启动器启动完成")

# 步骤2: 执行登录操作
print("\n步骤2: 执行登录操作")
print("提示: 此脚本使用坐标点击方式")
print("建议：在实际使用时，使用AirtestIDE的截图功能")
print("捕获账号登录按钮的图片，然后使用图像识别点击")

# 尝试点击屏幕中央位置
try:
    from airtest.core.api import touch
    
    # 尝试多个可能的位置
    possible_positions = [
        (960, 540),   # 1920x1080屏幕中央
        (683, 384),   # 1366x768屏幕中央
        (800, 450),   # 1600x900屏幕中央
        (1024, 576),  # 2048x1152屏幕中央
    ]
    
    print("尝试点击可能的账号登录按钮位置...")
    
    success_count = 0
    for i, pos in enumerate(possible_positions):
        try:
            touch(pos)
            print(f"✅ 点击位置 {pos} 成功")
            success_count += 1
            # 每次点击后等待2秒
            time.sleep(2)
        except Exception as e:
            print(f"❌ 点击位置 {pos} 失败: {e}")
    
    if success_count > 0:
        print("\n✅ 登录操作执行完成")
    else:
        print("\n⚠️  所有点击尝试失败，请检查设备连接")
except Exception as e:
    print(f"❌ 登录操作失败: {e}")

# 步骤3: 验证结果
print("\n步骤3: 验证结果")
print("⚠️  由于没有图像识别，无法自动验证登录是否成功")
print("请手动检查游戏启动器是否进入登录界面")

print("\n测试脚本执行完成！")
print("=" * 60)
print("\n在CMD中执行的注意事项：")
print("1. 确保Python已添加到系统环境变量")
print("2. 脚本路径中不要包含中文或空格")
print("3. 执行命令示例：")
print("   cd C:\\Users\\Administrator\\Documents\\trae_projects\\install")
print("   python eudemons_cmd_login.py")
print("\n如果仍然报错，请检查：")
print("- Python是否正确安装")
print("- Airtest是否正确安装")
print("- 游戏启动器路径是否正确")
