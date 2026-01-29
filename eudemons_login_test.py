from airtest.core.api import *
import time
import pywinauto
from pywinauto.application import Application

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

# 使用pywinauto查找窗口
print("查找游戏启动器窗口...")
try:
    # 尝试连接到已启动的应用
    print("尝试连接到游戏启动器窗口...")
    max_attempts = 5
    attempt = 0
    app = None
    
    while attempt < max_attempts:
        try:
            app = Application(backend="uia").connect(title_re="*魔域*")
            print("✅ 成功连接到游戏启动器窗口")
            break
        except Exception as e:
            attempt += 1
            print(f"连接失败，尝试 {attempt}/{max_attempts}: {e}")
            time.sleep(2)
    
    if not app:
        print("❌ 无法连接到游戏启动器窗口")
        # 尝试通过进程名连接
        try:
            print("尝试通过进程名连接...")
            # 查找包含"eudemons"的进程
            import psutil
            for proc in psutil.process_iter(['name']):
                if 'eudemons' in proc.info['name'].lower():
                    app = Application(backend="uia").connect(process=proc.pid)
                    print(f"✅ 通过进程 {proc.info['name']} 成功连接")
                    break
        except Exception as e:
            print(f"通过进程名连接失败: {e}")
    
    if not app:
        raise Exception("无法连接到游戏启动器")
    
    # 获取主窗口
    main_window = app.window(title_re="*魔域*")
    main_window.wait('visible', timeout=10)
    print(f"✅ 找到主窗口: {main_window.window_text()}")
    
    # 查找并点击账号登录按钮
    print("查找账号登录按钮...")
    
    # 尝试多种方式查找按钮
    login_button_names = ["账号登录", "登录", "accountLogin", "loginButton"]
    login_button = None
    
    # 尝试通过文本查找
    for btn_name in login_button_names:
        try:
            btn = main_window.child_window(title=btn_name, control_type="Button")
            if btn.exists():
                login_button = btn
                break
        except Exception:
            pass
    
    # 如果通过文本找不到，尝试通过类名查找
    if not login_button:
        try:
            # 枚举所有按钮
            buttons = main_window.descendants(control_type="Button")
            for btn in buttons:
                if btn.window_text() in login_button_names:
                    login_button = btn
                    break
        except Exception as e:
            print(f"枚举按钮失败: {e}")
    
    if login_button:
        print(f"✅ 找到账号登录按钮: {login_button.window_text()}")
        login_button.click()
        print("✅ 账号登录按钮点击成功")
        time.sleep(3)
        
        # 检查是否进入登录界面
        print("检查是否进入登录界面...")
        try:
            # 尝试查找账号输入框
            account_input = main_window.child_window(title="请输入账号", control_type="Edit")
            if account_input.exists():
                print("✅ 成功进入登录界面，找到账号输入框")
            else:
                # 尝试其他可能的输入框
                inputs = main_window.descendants(control_type="Edit")
                if inputs:
                    print("✅ 成功进入登录界面，找到输入框")
                else:
                    print("⚠️  未找到输入框，可能未成功进入登录界面")
        except Exception as e:
            print(f"检查登录界面失败: {e}")
    else:
        print("❌ 未找到账号登录按钮")
        # 尝试使用坐标点击（根据实际界面调整）
        print("尝试使用坐标点击...")
        # 这里的坐标需要根据实际界面调整
        touch((300, 200))
        print("已尝试坐标点击")
        time.sleep(3)
except Exception as e:
    print(f"❌ 操作失败: {e}")
    import traceback
    traceback.print_exc()

print("\n测试脚本执行完成！")
print("=" * 60)
