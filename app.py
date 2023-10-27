from flask import Flask, jsonify, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

from selenium import webdriver


@app.route('/get_schedule', methods=['GET'])
def hello_world():
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
        driver.execute_script("arguments[0].setAttribute('class','couple-faculty-level-education uncovered')",
                              element1[0])
        time.sleep(1)
        element2 = element1[0].find_elements(By.TAG_NAME, 'div')

        click_elem = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/span")

        driver.execute_script("arguments[0].click();", click_elem)
        time.sleep(5)
        table = driver.find_element(By.TAG_NAME, 'table')
        return f'<table> {table.get_attribute("innerHTML")} </table>'

    table = BeautifulSoup(get_ebuchaya_tablica())
    table_body = table.find('tbody')
    table_trs = table_body.findAll('tr')
    group = table_trs[0].findAll('th')[3].text
    data = []
    date = ("1", "2", "3", "4", "5", "6")
    from itertools import cycle
    iter_date = cycle(date)

    def pn():
        data = []
        for i in range(2, 7):
            try:
                l = {table_trs[i].findAll('th')[0].text: table_trs[i].findAll('td')[1].findAll('div')[0].get_text(
                    strip=True)}
            except:
                l = None
            data.append({
                next(iter_date): l
            })
        return data

    def vt():
        data = []
        for i in range(2, 7):
            try:
                l = {table_trs[i].findAll('th')[0].text: table_trs[i].findAll('td')[1].findAll('div')[0].get_text(
                    strip=True)}
            except:
                l = None
            data.append({
                next(iter_date): l
            })
        return data

    def sr():
        data = []
        for i in range(2, 7):
            try:
                l = {table_trs[i].findAll('th')[0].text: table_trs[i].findAll('td')[1].findAll('div')[0].get_text(
                    strip=True)}
            except:
                l = None
            data.append({
                next(iter_date): l
            })
        return data

    def cht():
        data = []
        for i in range(2, 7):
            try:
                l = {table_trs[i].findAll('th')[0].text: table_trs[i].findAll('td')[1].findAll('div')[0].get_text(
                    strip=True)}
            except:
                l = None
            data.append({
                next(iter_date): l
            })
        return data

    def pt():
        data = []
        for i in range(2, 7):
            try:
                l = {table_trs[i].findAll('th')[0].text: table_trs[i].findAll('td')[1].findAll('div')[0].get_text(
                    strip=True)}
            except:
                l = None
            data.append({
                next(iter_date): l
            })
        return data

    def sub():
        data = []
        for i in range(2, 7):
            try:
                l = {table_trs[i].findAll('th')[0].text: table_trs[i].findAll('td')[1].findAll('div')[0].get_text(
                    strip=True)}
            except:
                l = None
            data.append({
                next(iter_date): l
            })
        return data

    return render_template('index.html', jobj=str({group: {
        "Понедельник": pn(),
        "Вторник": vt(),
        "Среда": sr(),
        "Четверг": cht(),
        "Пятница": pt(),
        "Суббота": sub()
    }}))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

