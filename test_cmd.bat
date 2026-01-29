@echo off

echo 测试cmd执行Python脚本
echo ========================

REM 显示Python版本
python --version

REM 执行测试脚本
python cmd_test.py

REM 执行最终版登录脚本
echo.
echo 执行登录脚本:
echo ========================
python eudemons_final_login.py

echo.
echo 测试完成，按任意键退出...
pause > nul
