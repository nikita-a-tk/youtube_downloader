# https://www.youtube.com/playlist?list=PLC890D2C32BFBE0A5
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/playlist?list=PLC890D2C32BFBE0A5")
try:
    elements = WebDriverWait(driver, 3).until(
        EC.presence_of_all_elements_located((By.XPATH, "//a[@class='style-scope ytd-playlist-video-renderer']")) 
    )
    for e in elements:
    	print(e.text + " - " + e.get_attribute('href'))
finally:
    driver.quit()





# with urllib.request.urlopen('https://www.youtube.com/playlist?list=PLC890D2C32BFBE0A5') as page:
# 	text = page.read().decode('utf-8')
# parser = MyHTMLParser()
# parser.feed(text)



# import urllib.request
# from xml.dom.minidom import parse, parseString

# with urllib.request.urlopen('https://nikita-a-tk.github.io/') as page:
# 	text = page.read().decode('utf-8')
# 	my_dom = parseString(text)
# 	exp_table = my_dom.getElementsByTagName('table')
# 	print('\n' + exp_table)

