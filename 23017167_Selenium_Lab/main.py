#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Điểm khởi chạy kiểm thử tự động chính: python main.py"""
import run_tests

if __name__ == "__main__":
    run_tests.main() if hasattr(run_tests, 'main') else run_tests.run_test_suite()

