# -*- coding: utf-8 -*-
import logging
import time


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import config

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start_session(driver):
    url = "https://photos.google.com/login"
    logging.info("Getting URL")
    driver.get(url)

    logging.info("Filling user.")
    login = driver.find_element_by_name("identifier")
    login.send_keys(config.USER, Keys.RETURN)
    time.sleep(4)

    logging.info("Filling password.")
    pw = driver.find_element_by_name("password")
    pw.send_keys(config.PASSWORD, Keys.RETURN)
    time.sleep(20)


def delete_all_photos(driver):
    logging.debug("Switching to photos view.")
    url = "https://photos.google.com/u/1/"
    driver.get(url)
    time.sleep(20)

    logging.info("Starting to delete all Google Photos.")
    while True:
        try:
            # not the most elegant solution, but it works
            logging.debug("selecting some photos")
            select_button = driver.find_element_by_xpath(
                "//div[@role='checkbox']")
            driver.execute_script("arguments[0].click();", select_button)
            time.sleep(1.5)

            logging.debug("triggering delete for selected photos")
            del_button = driver.find_element_by_xpath(
                "//button[@title='Delete']")
            del_button.click()
            time.sleep(1.5)

            logging.debug("confirm delete")
            confirm_button = driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/div/div[2]/div[3]/button[2]")
            confirm_button.click()
        # navigating this DOM is hard, so we just keep trying
        except Exception as e:
            logging.debug(e)
            time.sleep(1)
        time.sleep(3)


def delete_all_suggestions(driver):
    logging.debug("Switching to assistant view.")
    working = [None]
    url = "https://photos.google.com/u/1/assistant"
    driver.get(url)
    while True:
        try:
            delete_buttons = driver.find_elements_by_xpath(
                "//button[@aria-label='Dismiss']")
            for delete_button in delete_buttons:
                delete_button.click()
                time.sleep(0.5)
        except Exception as e:
            logging.debug(e)
            time.sleep(1)
            working = [None]


if __name__ == '__main__':
    # replace with your favorite (supported) browser
    driver = webdriver.Firefox()
    # start a logged in session
    start_session(driver)

    # uncomment to delete all Google Assistant suggestions (montages of your photos)
    # delete_all_suggestions(driver)
    # deletes ALL your Google photos
    delete_all_photos(driver)
