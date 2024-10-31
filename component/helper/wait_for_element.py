import time

def wait_for_element(driver, locator, timeout=60):
    for _ in range(timeout):
        try:
            element = driver.find_element(*locator)
            return element
        except:
            time.sleep(1)
    raise Exception(f"Element {locator} not found after {timeout} seconds")

def wait_for_elements(driver, locator, timeout=30):
    for _ in range(timeout):
        try:
            element = driver.find_elements(*locator)
            return element
        except:
            time.sleep(1)
    raise Exception(f"Element {locator} not found after {timeout} seconds")
