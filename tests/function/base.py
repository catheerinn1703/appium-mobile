from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


def wait_until_text_visible(driver, text):
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//*[@text="{text}"]')))
        return element
    except TimeoutException as ex:
        # handle the exception here
        print("Element is not visible. " + str(ex))


def wait_until_id_visible(driver, value):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, value)))
        return element
    except TimeoutException as ex:
        # handle the exception here
        print("Element is not visible. " + str(ex))

def wait_until_visible_xpath(driver, value):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f'//*[@resource-id="{value}"]')))
        return element
    except TimeoutException as ex:
        # handle the exception here
        print("Element is not visible. " + str(ex))

def find_element_by_text(driver, text):
    try:
        button = driver.find_element(by=AppiumBy.XPATH, value=f'//*[@text="{text}"]')
        return button
    except NoSuchElementException:
        print(f"Element with text '{text}' not found")
        return None

def find_element_by_resource_id(driver, value):
    try:
        button = driver.find_element(by=AppiumBy.XPATH, value=f'//*[@resource-id="{value}"]')
        return button
    except NoSuchElementException:
        print(f"Resource Id with text '{value}' not found")
        return None

def find_element_by_hint(driver, text):
    try:
        button = driver.find_element(by=AppiumBy.XPATH, value=f'//*[@hint="{text}"]')
        return button
    except NoSuchElementException:
        print(f"Element with text '{text}' not found")
        return None


def click_by_text(driver, text):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//*[@text="{text}"]')))
    except TimeoutException as ex:
        # handle the exception here
        print("Exception has been thrown. " + str(ex))

    try:
        button = driver.find_element(by=AppiumBy.XPATH, value=f'//*[@text="{text}"]')
        button.click()
        return button
    except NoSuchElementException:
        print(f"Element with text '{text}' not found")


def click_save(driver):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//*[@text="SAVE"]')))
    except TimeoutException as ex:
        # handle the exception here
        print("Exception has been thrown. " + str(ex))

    try:
        button = driver.find_element(by=AppiumBy.XPATH, value=f'//*[@text="SAVE"]')
        button.click()
        return button
    except NoSuchElementException:
        print(f"Element with text 'SAVE' not found")
