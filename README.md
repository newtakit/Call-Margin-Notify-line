# Call-Margin-Notify-line
-- Notify-line-Call-Margin

"โปรเจคนี้มีเป้าหมายในการดึงข้อมูล call margin จากเว็บไซต์SET-Dinamiและนำไปแจ้งเตือนผ่านไลท์ "

--
## Tools

1. Python (ในตัวอย่างจะใช้ Version 3.13.1 / ระบบปฏิบัติการ windows 11)
2. Library ที่ต้องลงเพิ่ม
    1. selenium
    2. Pandas
    3. gspread
    4. webdriver
    

3. Visual Studio Code

## Process

1. ใช้ selenium  เพื่อ login หน้าเว็บ สำหรับพนักงานของ(CAF)
2. ใช้ selenium  เพื่อ Automationในการ cilck 
3. ดึง HTML จากองค์ประกอบที่มีตารางข้อมูล
4. แปลง HTML เป็น DataFrame ด้วย pandas
5. นำข้อมูลไปเก็บใน Google Sheets
6. ใช้ sheetapp เขียน code เพื่อส่งข้อมูลผ่าน API ผ่านไลท์

-- 1. ใช้ selenium  เพื่อ login หน้าเว็บ สำหรับพนักงานของ(CAF)


```
username = '******'
password = '*****'

driver = webdriver.Chrome()
driver.get('url')
time.sleep(5)

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
        print(" เข้าสู่ระบบสำเร็จ!")
    else:
        print(" ไม่สามารถเข้าสู่ระบบได้!")

except Exception as e:
    print(f" เกิดข้อผิดพลาด: {e}")
    driver.quit()



```
-- 2. ใช้ selenium  เพื่อ Automationในการ cilck 

```
WebDriverWait(driver, 10)until( 
        EC.presence_of_element_located((By.XPATH, xpath))
    ).click()
    time.sleep(2)

WebDriverWait(driver, 10)until( 
        EC.presence_of_element_located((By.XPATH, xpath))
    ).click()
    time.sleep(2)

```

#ไม่มั่นใจว่า  ตลาดกับทาง บริษัทจะอนญาติให้ทำในส่วนนี้ไหม หลังlogin เพราะการดึงข้อมูลหลังจากนี้ก็ไม่มีอะไรแล้ว 





-- 4. แปลง HTML เป็น DataFrame ด้วย pandas

```
time.sleep(10)  # รอให้ข้อมูลปรากฏ
element = driver.find_element(By.XPATH, '[]')
partial_html = element.get_attribute('outerHTML')  # ดึง HTML
data_df2 = pd.read_html(partial_html)[0]  # แปลง HTML เป็น DataFrame ด้วย pandas
print(data_df2.head(12))  # แสดงข้อมูลบางส่วนเพื่อความแน่ใจ

driver.quit()


```

--5. นำข้อมูลไปเก็บใน Google Sheets

```
scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
credentials = Credentials.from_service_account_file(
    r'C:/Users/newta/OneDrive/Desktop/new-git-test/web-dinami/credentials.json', scopes=scopes)

gc = gspread.authorize(credentials)

# เปิด Google Sheets
gs = gc.open_by_key('1ufmnoC_3ds_Gv9R0KvjN1GnIwHz8uCVdMTDib1Dlj_U')
worksheet1 = gs.worksheet('Sheet1')

# อัปโหลดข้อมูลจาก DataFrame ไปยัง Google Sheets
set_with_dataframe(worksheet1, data_df2)
print("อัปโหลดข้อมูลสำเร็จ!")

```
-- 6. ใช้ sheetapp เขียน code เพื่อส่งข้อมูลผ่าน API ผ่านไลท์
