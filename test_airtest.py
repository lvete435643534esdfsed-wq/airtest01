from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

print("Airtest 测试脚本")
print("=" * 50)

# 打印版本信息
import airtest
print(f"Airtest 版本: {airtest.__version__}")

try:
    import poco
    print(f"Poco 已安装成功!")
    # 尝试获取版本信息
    if hasattr(poco, '__version__'):
        print(f"Poco 版本: {poco.__version__}")
    else:
        print("Poco 版本信息不可用")
except ImportError as e:
    print(f"Poco 未安装: {e}")

print("=" * 50)
print("测试脚本执行完成！")
print("\n使用说明：")
print("1. 连接设备: connect_device('Android:///')")
print("2. 点击操作: touch((x, y)) 或 touch(Template('image.png'))")
print("3. 文本输入: text('Hello Airtest')")
print("4. 断言操作: assert_exists(Template('image.png'))")
print("\nAirtest IDE 安装建议：")
print("由于网络原因，建议手动访问 http://airtest.netease.com/ 下载")
print("下载后解压到任意目录，双击 AirtestIDE.exe 即可使用")
