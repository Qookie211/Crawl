from selenium import webdriver



driver = webdriver.Chrome()
driver.get("https://www.zhihu.com/explore")
Pow = driver.find_element_by_id("Popverl-toggle")
print(Pow.id)
print(Pow.location)
print(Pow.tag_name)
print(Pow.size)
driver.close()

