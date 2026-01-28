from airtest.core.api import *
from poco.drivers.windows import WindowsPoco
import time

print("魔域游戏启动器登录测试脚本")
print("=" * 60)

# 配置信息
APP_PATH = "D:\EudemonsLauncher\eudemons_launcher.exe"  # 魔域游戏启动器路径

# 连接Windows设备
print("连接Windows设备...")
connect_device("Windows:///")
time.sleep(2)

# 启动游戏启动器
print(f"启动魔域游戏启动器...")
start_app(APP_PATH)
time.sleep(10)  # 等待启动器启动完成

# 初始化Poco
print("初始化Poco...")
poco = WindowsPoco()
time.sleep(5)

# 查找并点击账号登录按钮
print("查找账号登录按钮...")
try:
    # 尝试多种方式查找账号登录按钮
    login_buttons = [
        poco("账号登录"),
        poco(text="账号登录"),
        poco(name="accountLoginButton"),
        poco(name="loginButton"),
        poco(text="登录")
    ]
    
    login_button = None
    for btn in login_buttons:
        if btn.exists():
            login_button = btn
            break
    
    if login_button:
        print("找到账号登录按钮，点击...")
        login_button.click()
        print("✅ 账号登录按钮点击成功")
        time.sleep(3)
        
        # 检查是否进入登录界面
        print("检查是否进入登录界面...")
        # 尝试查找账号输入框来确认
        account_inputs = [
            poco("账号输入框"),
            poco(text="请输入账号"),
            poco(name="accountInput")
        ]
        
        account_input = None
        for input_elem in account_inputs:
            if input_elem.exists():
                account_input = input_elem
                break
        
        if account_input:
            print("✅ 成功进入登录界面")
        else:
            print("⚠️  未找到账号输入框，可能未成功进入登录界面")
    else:
        print("❌ 未找到账号登录按钮")
        # 尝试使用坐标点击（根据实际界面调整）
        print("尝试使用坐标点击...")
        # 这里的坐标需要根据实际界面调整
        touch((300, 200))
        print("已尝试坐标点击")
        time.sleep(3)
except Exception as e:
    print(f"❌ 点击账号登录按钮失败: {e}")

print("\n测试脚本执行完成！")
print("=" * 60)
