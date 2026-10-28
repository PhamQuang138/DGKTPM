#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
SCRIPT THỰC THI KIỂM THỬ TỰ ĐỘNG WEB UI BẰNG SELENIUM & PYTEST
Môn học: Đánh giá và Kiểm định chất lượng phần mềm
Sinh viên: Phạm Duy Quang (MSSV: 23017167) - Lớp: AI&KHDL_1
Hệ thống thử nghiệm: Swag Labs (https://www.saucedemo.com/)
================================================================================
"""

import os
import sys
import time
import subprocess

# Cấu hình encoding UTF-8 tương thích tuyệt đối cho mọi terminal Windows (chống UnicodeEncodeError)
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Đường dẫn thư mục gốc của project
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_FILE = os.path.join(PROJECT_DIR, "tests", "test_saucedemo_cases.py")
REPORT_HTML = os.path.join(PROJECT_DIR, "reports", "selenium_report.html")
SCREENSHOTS_DIR = os.path.join(PROJECT_DIR, "reports", "screenshots")

def print_banner():
    banner = """
================================================================================
        BO KIEM THU TU DONG WEB UI - SELENIUM WEBDRIVER (PAGE OBJECT MODEL)
        Website muc tieu: https://www.saucedemo.com/ (Swag Labs)
        Sinh vien thuc hien: Pham Duy Quang - MSSV: 23017167 - Lop: AI&KHDL_1
================================================================================
"""
    print(banner)

def get_python_executable():
    """Tự động ưu tiên sử dụng Python trong môi trường ảo .venv nếu có"""
    venv_python = os.path.join(PROJECT_DIR, ".venv", "Scripts", "python.exe")
    if os.path.exists(venv_python):
        return venv_python
    venv_python_unix = os.path.join(PROJECT_DIR, ".venv", "bin", "python")
    if os.path.exists(venv_python_unix):
        return venv_python_unix
    return sys.executable

def ensure_dependencies():
    """Kiểm tra và xác nhận các thư viện bắt buộc đã được cài đặt"""
    print("[1/3] Kiem tra moi truong thuc thi va thu vien phu thuoc...")
    py_exec = get_python_executable()
    check_code = "import selenium, pytest, pytest_html; print('OK')"
    res = subprocess.run([py_exec, "-c", check_code], capture_output=True, text=True)
    if res.returncode != 0:
        print("[!] Phat hien thieu thu vien. Dang tu dong cai dat tu requirements.txt...")
        req_file = os.path.join(PROJECT_DIR, "requirements.txt")
        subprocess.run([py_exec, "-m", "pip", "install", "-r", req_file], check=True)
    else:
        print("  -> Moi truong san sang: Python, Selenium, Pytest, Pytest-HTML.")

def run_test_suite():
    """Chạy toàn bộ 06 ca kiểm thử tự động với Pytest và xuất báo cáo HTML"""
    print("\n[2/3] Bat dau thuc thi bo 06 Test Cases kiem thu tu dong...")
    print(f"  -> File kiem thu: {TEST_FILE}")
    print(f"  -> Bao cao HTML:  {REPORT_HTML}")
    print(f"  -> Thu muc anh:   {SCREENSHOTS_DIR}")
    print("-" * 80)

    py_exec = get_python_executable()
    os.makedirs(os.path.dirname(REPORT_HTML), exist_ok=True)
    os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

    # Lệnh thực thi pytest
    pytest_cmd = [
        py_exec, "-m", "pytest",
        TEST_FILE,
        "-v",
        "-s",
        f"--html={REPORT_HTML}",
        "--self-contained-html"
    ]

    start_time = time.time()
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    result = subprocess.run(pytest_cmd, cwd=PROJECT_DIR, env=env)
    duration = time.time() - start_time

    print("-" * 80)
    print(f"\n[3/3] Ket thuc thuc thi trong: {duration:.2f} giay")

    if result.returncode == 0:
        print("\n>>> KET QUA: 100% TEST CASES DAT CHUAN (ALL PASSED) <<<")
    else:
        print(f"\n>>> KET QUA: CO LOI XAY RA (Exit code: {result.returncode}) <<<")

    print(f"Bao cao chi tiet dang HTML da luu tai: {REPORT_HTML}")
    print(f"Anh chup man hinh minh chung da luu tai: {SCREENSHOTS_DIR}\n")
    return result.returncode

def main():
    print_banner()
    ensure_dependencies()
    code = run_test_suite()
    return code

if __name__ == "__main__":
    sys.exit(main())
