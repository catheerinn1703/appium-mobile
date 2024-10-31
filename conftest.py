import os
import subprocess
import time

import emulator
import pytest
import requests
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions
import logging

from appium.webdriver.appium_service import AppiumService

from config.desired_capabilities import multiple_emulators, android_13
from data.test_data import appium_server


# appium_server_url = 'http://localhost:4723'


@pytest.fixture(scope="module")
def headers_without_auth():
    return {
        "Content-Type": "application/json",
        "Accept-Language": "en"
    }


def login(headers_without_auth, payload):
    url = 'https://sqemp-be.stg.squantumengine.com/'
    path = "v1/auth/login"
    response = requests.post(url=url + path, headers=headers_without_auth, json=payload)

    return response


@pytest.fixture(scope="module")
def get_access_token(headers_without_auth):
    payload = {
        "email": "qa@gmail.com",
        "password": "sqemp_qa123"
    }

    response = login(headers_without_auth, payload)
    data = response.json()
    access_token = data["token"]["access_token"]
    return access_token


# for reuse access_token
token = ""


@pytest.fixture(scope="module")
def headers(get_access_token):
    if token == "":
        return {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + get_access_token,
            "Accept-Language": "en"
        }
    else:
        return token


# Mobile Fixture
@pytest.fixture(scope='session')
def appium_service():
    service = AppiumService()
    service.start()
    print("Appium service has started...")
    yield service
    service.stop()
    print("Appium service has stopped...")


# Logging info
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def single_driver_permission_true():
    subprocess.run(["pkill", "-9", "-f", "appium"])
    print("Kill leftover appium server")

    service = AppiumService()
    service.start(args=['--log', 'appium_service.log'])
    print("Appium service has started...")
    time.sleep(10)

    device = android_13()
    appium_options = UiAutomator2Options()
    appium_options.load_capabilities(device)
    time.sleep(10)

    try:
        driver = webdriver.Remote(appium_server, options=appium_options, direct_connection=True)
        time.sleep(10)
        # driver.implicitly_wait(10)

        # Grant permission to post notification from emulator
        subprocess.run(["adb", "-s", device["deviceName"], "shell", "pm", "grant", device["appPackage"],
                        "android.permission.POST_NOTIFICATIONS"])
        print("Grant permission to post notifications")

        yield driver
        driver.quit()
        print(driver)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        subprocess.run(["adb", "-s", device['deviceName'], "emu", "kill"])
        print("emulator closing")
        service.stop()
        print("Appium Service Stopping")
        subprocess.run(["pkill", "-f", "appium"])
        print("Kill leftover appium server")
        time.sleep(5)


@pytest.fixture(scope='session', params=multiple_emulators())
def create_android_drivers(request):
    device = request.param

    service = AppiumService()
    service.start(args=['--log', 'appium_service.log'])
    print("Appium service has started...")
    time.sleep(10)

    appium_options = UiAutomator2Options()
    appium_options.load_capabilities(device)
    time.sleep(10)

    try:
        driver = webdriver.Remote(appium_server, options=appium_options, direct_connection=True)
        driver.implicitly_wait(10)

        # Grant permission to post notification from emulator
        subprocess.run(["adb", "-s", device["deviceName"], "shell", "pm", "grant", device["appPackage"],
                        "android.permission.POST_NOTIFICATIONS"])
        print("Grant permission to post notifications")

        yield driver
        driver.quit()
        print(driver)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        os.system("adb -s emulator-5554 emu kill")
        print("emulator closing")
        service.stop()
        print("Appium Service Stopping")
        subprocess.run(["pkill", "-f", "appium"])
        print("Kill leftover appium server")
        time.sleep(10)
