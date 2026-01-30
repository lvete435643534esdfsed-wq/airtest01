from airtest.core.api import *
import os
import logging
import time

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('eudemons_test.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def eudemons_login_test():
    """Eudemons登录测试脚本"""
    try:
        logger.info("开始Eudemons登录测试")
        
        # 连接Windows设备
        logger.info("连接Windows设备")
        dev = connect_device("Windows:///")
        logger.info(f"设备连接成功: {dev}")
        
        # 启动eudemons_launcher.exe
        logger.info("启动eudemons_launcher.exe")
        launcher_path = r"C:\path\to\eudemons_launcher.exe"  # 请替换为实际路径
        
        if not os.path.exists(launcher_path):
            logger.error(f"启动器文件不存在: {launcher_path}")
            return False
        
        os.startfile(launcher_path)
        logger.info("启动器启动成功")
        
        # 等待启动器加载
        time.sleep(10)
        logger.info("等待启动器加载完成")
        
        # 点击登录按钮
        logger.info("点击登录按钮")
        login_btn = Template(r"login_btn.png", threshold=0.8)
        if exists(login_btn):
            touch(login_btn)
            logger.info("登录按钮点击成功")
        else:
            logger.error("未找到登录按钮")
            return False
        
        # 等待登录界面加载
        time.sleep(3)
        
        # 输入账号密码
        logger.info("输入账号密码")
        # 假设账号输入框和密码输入框的位置
        account_input = Template(r"account_input.png", threshold=0.8)
        password_input = Template(r"password_input.png", threshold=0.8)
        
        if exists(account_input):
            touch(account_input)
            text("your_account")  # 请替换为实际账号
            logger.info("账号输入成功")
        else:
            logger.error("未找到账号输入框")
            return False
        
        if exists(password_input):
            touch(password_input)
            text("your_password")  # 请替换为实际密码
            logger.info("密码输入成功")
        else:
            logger.error("未找到密码输入框")
            return False
        
        # 点击确认登录
        logger.info("点击确认登录")
        confirm_btn = Template(r"confirm_btn.png", threshold=0.8)
        if exists(confirm_btn):
            touch(confirm_btn)
            logger.info("确认登录按钮点击成功")
        else:
            logger.error("未找到确认登录按钮")
            return False
        
        # 等待登录完成
        time.sleep(15)
        logger.info("等待登录完成")
        
        # 验证登录是否成功
        logger.info("验证登录是否成功")
        success_indicator = Template(r"success_indicator.png", threshold=0.8)
        if exists(success_indicator):
            logger.info("登录成功！")
            return True
        else:
            logger.error("登录失败，未找到成功标识")
            return False
            
    except Exception as e:
        logger.error(f"测试过程中出现错误: {str(e)}")
        import traceback
        logger.error(traceback.format_exc())
        return False
    finally:
        logger.info("测试结束")
        # 生成测试报告
        logger.info("生成测试报告")
        try:
            from airtest.report.report import simple_report
            simple_report(__file__, logpath=None, output="eudemons_test_report.html")
            logger.info("测试报告生成成功: eudemons_test_report.html")
        except Exception as e:
            logger.error(f"生成测试报告失败: {str(e)}")

if __name__ == "__main__":
    logger.info("=== Eudemons每日登录测试脚本 ===")
    result = eudemons_login_test()
    if result:
        logger.info("测试通过！")
        exit(0)
    else:
        logger.error("测试失败！")
        exit(1)