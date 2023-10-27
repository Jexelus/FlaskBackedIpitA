def get_ebuchaya_tablica():
    from selenium import webdriver
    from selenium.webdriver import ActionChains
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    import time

    driver = webdriver.Chrome()
    driver.get('https://tsput.ru/student/schedule/current_schedule.php')
    element = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/div[2]/div/div[2]")
    driver.execute_script("arguments[0].setAttribute('class','couple-faculty-item uncovered')", element)
    time.sleep(1)
    element1 = element.find_elements(By.TAG_NAME, 'div')
    driver.execute_script("arguments[0].setAttribute('class','couple-faculty-level-education uncovered')", element1[0])
    time.sleep(1)
    element2 = element1[0].find_elements(By.TAG_NAME, 'div')

    click_elem = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/span")

    driver.execute_script("arguments[0].click();", click_elem)
    time.sleep(5)
    table = driver.find_element(By.TAG_NAME, 'table')
    return f'<table> {table.get_attribute("innerHTML")} </table>'

get_ebuchaya_tablica()
