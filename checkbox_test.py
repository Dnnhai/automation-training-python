from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/checkboxes")

elements = driver.find_elements_by_xpath("//*[@id=\"checkboxes\"]/input")

driver.close()
driver.quit()
