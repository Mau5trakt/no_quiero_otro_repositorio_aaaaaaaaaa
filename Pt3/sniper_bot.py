from time import sleep
from requests_html import HTMLSession
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

url = "https://www.pccomponentes.com/asus-geforce-gtx-1050-tis-4gb-gddr5"
url_coolmod = "https://www.coolmod.com/msi-gf65-thin-10ue-035xes-i5-10200h-rtx-3060-max-q-16gb-512gb-nvme-freedos-156-144hz-portatil-precio"

session = HTMLSession()

"""
while True:
    r = session.get(url)
    buy_zone = r.html.find("#btnsWishAddBuy")
    if len(buy_zone) > 0:
        print("HAY STOCK!!!")
        break
    else:
        print("Sigue sin haber stock :(")
    sleep(30)
"""

product_page = session.get(url_coolmod)
found = product_page.html.find("#main-buy")

if len(found) > 0:
    driver = webdriver.Chrome
    driver.get(url_coolmod)
    driver.find_element_by_class_name("confirm").click()
    driver.find_element_by_class_name("accept").click()
    driver.find_element_by_class_name("button-buy").click()
    sleep(1)
    driver.find_element_by_class_name("confirm").click()

    # Esto es por si vuelve a salir la silla razer
    try:
        driver.find_element_by_class_name("confirm").click()
    except NoSuchElementException:
        print("No habia silla razer")

    driver.find_element_by_class_name("button-buy").click()

    is_form_loaded = False
    form = None

    while not is_form_loaded:
        try:
            form = driver.find_element_by_class_name("login100-form")
            is_form_loaded = True
        except NoSuchElementException:
            print("Puessss no esta el formulario...")

    email = form.find_element_by_name("jform[email]")
    password = form.find_element_by_name("jform[password]")

    email.send_keys("nate@nate.com")
    password.send_keys("megustarazer")

    driver.find_element_by_class_name("login100-form-btn").click()

