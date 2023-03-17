import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import pandas as pd

#argument setting
#isProd = sys.argv[1]
url = sys.argv[1]
loginAccount = sys.argv[2]
saveFilePath = sys.argv[3]
ieDriverPath = sys.argv[4]

#browser and driver setting, open browser
ie_options = webdriver.IeOptions()
ie_options.attach_toe_dge_chrome = True
ie_options.edge_executable_path = “C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe”
driver = webdriver.Ie(executable_path= ieDriverPath, options=ie_options)
driver.get(url)

#selenium execution
elem = driver.find_element(By.LINK_TEXT, ‘[ 知識管理M000 ]’).click()
elem = driver.find_element(By.ID, ‘item1_8’).click()
elem = driver.find_element(By.ID, ‘item1_8_1’).click()

#get table info by bs4
soup = BeautifulSoup(driver.page_source, ‘html.parser’)
table = soup.find(‘table’, {‘id’: ‘GridView1’})

#save excel file by pandas
df = pd.read_html(str(table))[0]
df.to_excel(saveFilePath, index = False)

#close browser and driver
driver.quit()
