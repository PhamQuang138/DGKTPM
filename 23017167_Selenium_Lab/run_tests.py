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
from datetime import datetime

# Đường dẫn thư mục gốc của project
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_FILE = os.path.join(PROJECT_DIR, "tests", "test_saucedemo_cases.py")
REPORT_HTML = os.path.join(PROJECT_DIR, "reports", "selenium_report.html")
SCREENSHOTS_DIR = os.path.join(PROJECT_DIR, "reports", "screenshots")

def print_banner():
    banner = """
================================================================================
        BỘ KIỂM THỬ TỰ ĐỘNG WEB UI - SELENIUM WEBDRIVER (PAGE OBJECT MODEL)
        Website mục tiêu: https://www.saucedemo.com/ (Swag Labs)
        Sinh viên thực hiện: Phạm Duy Quang - MSSV: 23017167
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
    print("[1/3] Đang kiểm tra môi trường thực thi và thư viện phụ thuộc...")
    py_exec = get_python_executable()
    check_code = "import selenium, pytest, pytest_html; print('OK')"
    res = subprocess.run([py_exec, "-c", check_code], capture_output=True, text=True)
    if res.returncode != 0:
        print("[!] Phát hiện thiếu thư viện. Đang tự động cài đặt từ requirements.txt...")
        req_file = os.path.join(PROJECT_DIR, "requirements.txt")
        subprocess.run([py_exec, "-m", "pip", "install", "-r", req_file], check=True)
    else:
        print("  -> Môi trường đã sẵn sàng: Python, Selenium, Pytest, Pytest-HTML.")

def run_test_suite():
    """Chạy toàn bộ 06 ca kiểm thử tự động với Pytest và xuất báo cáo HTML"""
    print("\n[2/3] Bắt đầu thực thi bộ 06 Test Cases kiểm thử tự động...")
    print(f"  -> File kiểm thử: {TEST_FILE}")
    print(f"  -> Báo cáo HTML: {REPORT_HTML}")
    print(f"  -> Thư mục ảnh chụp: {SCREENSHOTS_DIR}")
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
    result = subprocess.run(pytest_cmd, cwd=PROJECT_DIR)
    duration = time.time() - start_time

    print("-" * 80)
    print(f"\n[3/3] Kết thúc thực thi trong: {duration:.2f} giây")

    if result.returncode == 0:
        print("\n>>> KẾT QUẢ: 100% TEST CASES ĐẠT CHUẨN (ALL PASSED) <<<")
    else:
        print(f"\n>>> KẾT QUẢ: CÓ LỖI XẢY RA (Mã lỗi exit code: {result.returncode}) <<<")

    print(f"Báo cáo chi tiết dạng HTML đã lưu tại: {REPORT_HTML}")
    print(f"Ảnh chụp màn hình minh chứng đã lưu tại: {SCREENSHOTS_DIR}\n")
    return result.returncode

if __name__ == "__main__":
    print_banner()
    ensure_dependencies()
    code = run_test_suite()
    sys.exit(code)
