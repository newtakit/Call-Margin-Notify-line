from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe
from google.oauth2.service_account import Credentials
import time
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive 

# ขั้นตอนที่ 1: ดึงข้อมูลจากหน้าเว็บ
driver = webdriver.Chrome()
driver.get('https://wwwa1.settrade.com/S16_MktRepLogin.jsp?txtBrokerId=063')