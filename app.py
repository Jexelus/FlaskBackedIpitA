from collections.abc import Callable, Iterable, Mapping
from typing import Any
from flask import Flask, jsonify, render_template
import requests
from bs4 import BeautifulSoup
import json
from threading import Thread

app = Flask(__name__)

from selenium import webdriver


class Shedule_Updater(Thread):
    def __init__(self):
        super().__init__()

    def update_schedule(self):
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
            data = dict()
            for i in range(2, 8):
                try:
                    l = {table_trs[i].findAll('th')[0].text: table_trs[i].findAll('td')[1].findAll('div')[0].get_text(
                        strip=True)}
                except:
                    l = None
                data[str(next(iter_date))] = l
            return data

        def vt():
            data = dict()
            for i in range(2, 8):
                try:
                    l = {table_trs[i].findAll('th')[0].text: table_trs[i].findAll('td')[1].findAll('div')[0].get_text(
                        strip=True)}
                except:
                    l = None
                data[str(next(iter_date))] = l
            return data

        def sr():
            data = {}
            for i in range(2, 8):
                try:
                    l = {table_trs[i].findAll('th')[0].text: table_trs[i].findAll('td')[1].findAll('div')[0].get_text(
                        strip=True)}
                except:
                    l = None
                data[str(next(iter_date))] = l
            return data

        def cht():
            data = {}
            for i in range(2, 8):
                try:
                    l = {table_trs[i].findAll('th')[0].text: table_trs[i].findAll('td')[1].findAll('div')[0].get_text(
                        strip=True)}
                except:
                    l = None
                data[str(next(iter_date))] = l
            return data

        def pt():
            data = {}
            for i in range(2, 8):
                try:
                    l = {table_trs[i].findAll('th')[0].text: table_trs[i].findAll('td')[1].findAll('div')[0].get_text(
                        strip=True)}
                except:
                    l = None
                data[str(next(iter_date))] = l
            return data

        def sub():
            data = {}
            for i in range(2, 8):
                try:
                    l = {table_trs[i].findAll('th')[0].text: table_trs[i].findAll('td')[1].findAll('div')[0].get_text(
                        strip=True)}
                except:
                    l = None
                data[str(next(iter_date))] = l
            return data

        with open('shedule_1.json', 'w') as f:
            data = {group: {
            "Понедельник": pn(),
            "Вторник": vt(),
            "Среда": sr(),
            "Четверг": cht(),
            "Пятница": pt(),
            "Суббота": sub()}}
            json.dump(data, 
            f, 
            indent=4, 
            ensure_ascii=False)
            f.close()

    def run(self):
        import time
        while True:
            try:
                self.update_schedule()
                time.sleep(300)
                print('|||||| shedule update operation complited sleep 5 mins ||||||')
            except Exception as e:
                print(f'|||||| error on update schedule |||||| --> {e}')
                time.sleep(300)

@app.route('/MOIS', methods=['GET'])
def MOIS():
    try:
        with open('shedule_1.json', 'r') as f:
            shedule = json.load(f)
            f.close()
        return jsonify(shedule)
    except Exception as e:
        print(f'|||||| error load shedule ||||||')
        return jsonify({'msg':'empty'})

if __name__ == '__main__':
    sub_thread = Shedule_Updater()
    sub_thread.daemon = True
    sub_thread.start()
    app.run(host='0.0.0.0', port=5000)

