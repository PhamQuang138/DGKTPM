@echo off
chcp 65001 > nul
echo ==============================================================================
echo   CHẠY KIỂM THỬ TỰ ĐỘNG SELENIUM WEBDRIVER (SWAG LABS - SAUCEDEMO)
echo   Sinh viên: Phạm Duy Quang - MSSV: 23017167 - Lớp: AI&KHDL_1
echo ==============================================================================
echo.

cd /d "%~dp0"

if exist ".venv\Scripts\python.exe" (
    echo [INFO] Sử dụng môi trường ảo Python .venv
    ".venv\Scripts\python.exe" run_tests.py
) else (
    echo [INFO] Sử dụng Python hệ thống
    python run_tests.py
)

pause

