from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def create_driver():
    # 1. 配置浏览器选项 (Options)
    chrome_options = Options()
    # 隐藏自动化标志，防止网站检测到你是 Bot
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    # 窗口最大化，避免元素因为屏幕宽度不够而被隐藏
    chrome_options.add_argument("--start-maximized")
    # 实验性选项：排除检测标志
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    # 2. 自动管理驱动 (Service)
    # 使用 webdriver-manager 自动下载并管理匹配的驱动版本
    service = Service(ChromeDriverManager().install())

    # 3. 实例化浏览器 (Instance)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    return driver
