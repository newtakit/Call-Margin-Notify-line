from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe
from google.oauth2.service_account import Credentials
import time
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive 

username = '******'
password = '*****'



#  ขั้นตอนที่ 2: ดึงข้อมูลจากหน้าเว็บ
driver = webdriver.Chrome()
driver.get('url')
time.sleep(5)

# กรอกข้อมูลการเข้าสู่ระบบ
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/table[4]/tbody/tr/td[2]/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td[4]/input'))
    ).send_keys(username)
    time.sleep(2)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="txtPassword"]'))
    ).send_keys(password)
    time.sleep(2)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="txtPassword"]'))
    ).send_keys(Keys.ENTER)  # กด Enter หลังจากกรอกรหัสผ่าน

    # ตรวจสอบว่ามีข้อความแจ้งเตือน "รหัสผิด" ปรากฏหรือไม่
    time.sleep(3)  # รอให้ระบบตอบกลับ

    success_check = driver.find_elements(By.XPATH, '//td[contains(text(), "หน้าแรก") or contains(text(), "ยินดีต้อนรับ")]')  # เปลี่ยน XPath ให้ตรงกับหน้าเว็บจริง

    if success_check:
        print("✅ เข้าสู่ระบบสำเร็จ!")
    else:
        print("❌ ไม่สามารถเข้าสู่ระบบได้!")

except Exception as e:
    print(f"🚨 เกิดข้อผิดพลาด: {e}")
    driver.quit()