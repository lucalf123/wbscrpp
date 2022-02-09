from openpyxl import Workbook
from selenium import webdriver
from lxml import html
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.amazon.com.br/s?k=iphone")

sleep(1)

tree = html.fromstring(driver.page_source)
wb = Workbook()
wb['Sheet'].title = "Produto"
sh1 = wb.active

for product_tree in tree.xpath('//div[contains(@data-cel-widget, "search_result_")]'):
    title = product_tree.xpath('.//span[@class="a-size-base-plus a-color-base a-text-normal"]/text()')
    price = product_tree.xpath('.//span[@class="a-price-whole"]/text()')

    data = list(zip(title, price))

    for i in data:
        sh1.append(i)
    wb.save("IphoneWSteste.xlsx")

driver.close()

