from selenium import webdriver

import time

import os

EMAIL = None
PASSWORD = None
if not EMAIL:
    raise ValueError("Must set e-mail")

if not PASSWORD:
    raise ValueError("Must set password")


def poll():

    driver = webdriver.Chrome()
    driver.get("http://www.amazon.com")

    driver.refresh()

    driver.implicitly_wait(5)
    sign_in = driver.find_element_by_link_text("Sign in")
    sign_in.click()

    time.sleep(2)
    e_mail_field = driver.find_element_by_id("ap_email")
    e_mail_field.send_keys(EMAIL)
    time.sleep(2)
    continue_button = driver.find_element_by_id("continue")
    continue_button.click()
    time.sleep(2)

    password_field = driver.find_element_by_id("ap_password")
    password_field.send_keys(PASSWORD)

    time.sleep(2)

    sign_in = driver.find_element_by_id("signInSubmit")
    sign_in.click()
    time.sleep(2)

    nav_cart = driver.find_element_by_id("nav-cart")
    nav_cart.click()

    time.sleep(2)

    proceed = driver.find_element_by_xpath("//input[starts-with(@name, 'proceedToALMCheckout-')]")
    proceed.click()

    time.sleep(2)

    continue_link = driver.find_element_by_name("proceedToCheckout")
    continue_link.click()

    time.sleep(2)
    count = 0
    while True:
        body = driver.find_element_by_tag_name("body")

        if "No delivery windows available." in body.text:
            count += 1
            print("No deliveries found. Attempt: %d" % count)
            time.sleep(30)
            driver.refresh()
        else:
            break

    os.system('say "Slots slots slots. Get over here. Get over here."')
    os.system('say "Slots slots slots. Get over here. Get over here."')
    os.system('say "Slots slots slots. Get over here. Get over here."')
    os.system('say "Slots slots slots. Get over here. Get over here."')
    while True:
        pass


if __name__ == '__main__':
    try:
        poll()
    except:
        os.system('say "Sorry, I appear to have died."')


