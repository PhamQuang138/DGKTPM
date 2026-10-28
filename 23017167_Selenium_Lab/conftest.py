import os
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

@pytest.fixture(scope="function")
def driver():
    """Khởi tạo Selenium WebDriver cho Microsoft Edge ở chế độ Headless"""
    edge_options = EdgeOptions()
    edge_options.add_argument("--headless=new")
    edge_options.add_argument("--window-size=1920,1080")
    edge_options.add_argument("--disable-gpu")
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")
    edge_options.add_argument("--disable-extensions")
    edge_options.add_argument("--log-level=3")
    
    # Đường dẫn cài đặt Edge mặc định trên Windows
    edge_bin = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    if os.path.exists(edge_bin):
        edge_options.binary_location = edge_bin

    # Selenium 4.6+ tự động quản lý EdgeDriver qua Selenium Manager
    driver = webdriver.Edge(options=edge_options)
    driver.implicitly_wait(10)
    
    yield driver
    
    driver.quit()

