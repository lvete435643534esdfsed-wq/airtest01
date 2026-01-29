from airtest.core.api import *
import time
import os
from airtest.report.report import simple_report

connect_device("Windows:///")
os.startfile(r"D:\EudemonsLauncher\eudemons_launcher.exe")
time.sleep(5)  # 给足够的时间让启动器加载
touch(Template('tpl1769599352442.png'))

touch(Template(r"tpl1769654288093.png", record_pos=(0.002, -0.061), resolution=(1572, 945)))
keyevent("tqnd233776")
touch(Template(r"tpl1769654346138.png", record_pos=(0.002, -0.026), resolution=(1572, 945)))
keyevent("HHj851224??")
touch(Template(r"tpl1769654367435.png", record_pos=(0.0, 0.04), resolution=(1572, 945)))
