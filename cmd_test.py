# 测试脚本，用于检查cmd执行环境
print("测试cmd执行环境")
print("=" * 50)

# 导入必要的模块
try:
    import sys
    import os
    print(f"Python版本: {sys.version}")
    print(f"Python路径: {sys.executable}")
    print(f"当前目录: {os.getcwd()}")
    print("✅ 基础模块导入成功")
except Exception as e:
    print(f"❌ 基础模块导入失败: {e}")

# 测试Airtest导入
try:
    from airtest.core.api import *
    print("✅ Airtest导入成功")
except Exception as e:
    print(f"❌ Airtest导入失败: {e}")

# 测试设备连接
try:
    connect_device("Windows:///")
    print("✅ 设备连接成功")
except Exception as e:
    print(f"❌ 设备连接失败: {e}")

print("=" * 50)
print("测试完成!")
