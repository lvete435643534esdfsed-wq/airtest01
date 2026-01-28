from airtest.core.api import *
from poco.drivers.windows import WindowsPoco
import time

print("魔域游戏自动登录测试脚本")
print("=" * 60)

# 配置信息
APP_PATH = "D:\EudemonsLauncher\playgame.exe"  # 魔域游戏启动器路径
ACCOUNT = "tqnd233776"
PASSWORD = "HHj851224??"

# 连接Windows设备
print("连接Windows设备...")
connect_device("Windows:///")
time.sleep(2)

# 启动游戏
print(f"启动魔域游戏...")
start_app(APP_PATH)
time.sleep(10)  # 等待游戏启动完成

# 初始化Poco
print("初始化Poco...")
poco = WindowsPoco()
time.sleep(5)

# 开始登录流程
print("开始登录流程...")

# 步骤1: 选择账号登录
try:
    # 查找账号登录按钮
    login_btn = poco("账号登录")
    if login_btn.exists():
        login_btn.click()
        print("点击账号登录按钮")
        time.sleep(3)
    else:
        print("账号登录按钮未找到，尝试其他方式")
        # 可能需要先点击登录按钮
        try:
            start_login_btn = poco("登录")
            if start_login_btn.exists():
                start_login_btn.click()
                print("点击登录按钮")
                time.sleep(3)
        except Exception as e:
            print(f"查找登录按钮失败: {e}")
except Exception as e:
    print(f"选择账号登录失败: {e}")

# 步骤2: 输入账号
try:
    # 查找账号输入框
    account_input = poco("账号输入框")
    if not account_input.exists():
        # 尝试其他可能的账号输入框标识
        account_input = poco(text="请输入账号")
    if not account_input.exists():
        account_input = poco(name="accountInput")
    
    if account_input.exists():
        account_input.set_text(ACCOUNT)
        print(f"输入账号: {ACCOUNT}")
        time.sleep(2)
    else:
        print("账号输入框未找到，尝试点击输入区域")
        # 尝试点击可能的账号输入区域
        try:
            # 假设账号输入框在特定位置
            touch((300, 200))  # 根据实际位置调整
            text(ACCOUNT)
            print(f"通过坐标输入账号: {ACCOUNT}")
            time.sleep(2)
        except Exception as e:
            print(f"输入账号失败: {e}")
except Exception as e:
    print(f"输入账号失败: {e}")

# 步骤3: 输入密码
try:
    # 查找密码输入框
    password_input = poco("密码输入框")
    if not password_input.exists():
        # 尝试其他可能的密码输入框标识
        password_input = poco(text="请输入密码")
    if not password_input.exists():
        password_input = poco(name="passwordInput")
    
    if password_input.exists():
        password_input.set_text(PASSWORD)
        print("输入密码: ******")
        time.sleep(2)
    else:
        print("密码输入框未找到，尝试点击输入区域")
        # 尝试点击可能的密码输入区域
        try:
            # 假设密码输入框在特定位置
            touch((300, 250))  # 根据实际位置调整
            text(PASSWORD)
            print("通过坐标输入密码: ******")
            time.sleep(2)
        except Exception as e:
            print(f"输入密码失败: {e}")
except Exception as e:
    print(f"输入密码失败: {e}")

# 步骤4: 点击登录按钮
try:
    # 查找登录按钮
    submit_btn = poco("登录")
    if not submit_btn.exists():
        submit_btn = poco(text="登录")
    if not submit_btn.exists():
        submit_btn = poco(name="loginButton")
    
    if submit_btn.exists():
        submit_btn.click()
        print("点击登录按钮")
        time.sleep(10)
    else:
        print("登录按钮未找到，尝试点击确认按钮")
        # 尝试点击确认按钮
        try:
            confirm_btn = poco("确认")
            if confirm_btn.exists():
                confirm_btn.click()
                print("点击确认按钮")
                time.sleep(10)
        except Exception as e:
            print(f"点击确认按钮失败: {e}")
except Exception as e:
    print(f"点击登录按钮失败: {e}")

# 步骤5: 检查是否登录成功
try:
    # 查找游戏主界面元素，确认登录成功
    # 这里需要根据实际游戏界面调整
    main_ui_element = poco("游戏主界面")
    if not main_ui_element.exists():
        # 尝试其他可能的主界面元素
        main_ui_element = poco(text="角色")
    if not main_ui_element.exists():
        main_ui_element = poco(name="mainUI")
    
    if main_ui_element.exists():
        print("\n✅ 登录成功！进入游戏主界面")
    else:
        print("\n⚠️  登录可能失败，未找到游戏主界面元素")
        # 检查是否有错误提示
        try:
            error_msg = poco("错误提示")
            if error_msg.exists():
                print(f"错误提示: {error_msg.get_text()}")
        except Exception as e:
            print(f"检查错误提示失败: {e}")
except Exception as e:
    print(f"检查登录状态失败: {e}")

print("\n测试脚本执行完成！")
print("=" * 60)
