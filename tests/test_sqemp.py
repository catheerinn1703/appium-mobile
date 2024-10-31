import subprocess
import time

from appium.options.android import UiAutomator2Options
from appium import webdriver

from component.api.send_push_notif import send_push_notif
from data.test_data import channel_id
from tests.function.base import click_by_text, wait_until_text_visible, find_element_by_text, wait_until_visible_xpath
from tests.function.mp import sqemp_mobile_setup


def test_send_push_notification_successfully(headers, create_android_drivers):
    time.sleep(5)
    # mobile secrets setup
    sqemp_mobile_setup(create_android_drivers)

    # register user
    wait_until_text_visible(create_android_drivers, "Input your User Id here")
    find_element_by_text(create_android_drivers, "Input your User Id here").send_keys("automation")
    click_by_text(create_android_drivers, "REGISTER PUSH NOTIFICATION")

    # assert push notification successfully sent from mobile
    success_popup = wait_until_text_visible(create_android_drivers, "Register Push Notification succeeds")
    assert success_popup.is_displayed()
    click_by_text(create_android_drivers, "OK")
    #
    # # trigger push notification API
    # time.sleep(10)
    # send_push_notif(headers, channel_id, "automation")
    #
    # time.sleep(20)
    # success_pn = wait_until_visible_xpath(create_android_drivers, "android:id/message")
    # assert success_pn.is_displayed()
    # click_by_text(create_android_drivers, "OK")
    #
    # # open notification panel
    # create_android_drivers.open_notifications()
    # pn = wait_until_text_visible(create_android_drivers,
    #                              "This is push notification for SQEMP mobile application")
    # assert pn.is_displayed()
    # create_android_drivers.press_keycode(3)


def test_send_pn_successfully_on_single_device(headers, single_driver_permission_true):
    time.sleep(5)
    # mobile secrets setup
    sqemp_mobile_setup(single_driver_permission_true)

    # register user
    wait_until_text_visible(single_driver_permission_true, "Input your User Id here")
    find_element_by_text(single_driver_permission_true, "Input your User Id here").send_keys("automation")
    click_by_text(single_driver_permission_true, "REGISTER PUSH NOTIFICATION")

    # assert push notification successfully sent from mobile
    success_popup = wait_until_text_visible(single_driver_permission_true, "Register Push Notification succeeds")
    assert success_popup.is_displayed()
    click_by_text(single_driver_permission_true, "OK")

    # trigger push notification API
    time.sleep(10)
    send_push_notif(headers, channel_id, "automation")
    send_push_notif(headers, channel_id, "automation")

    time.sleep(30)
    notifications = single_driver_permission_true.execute_script('mobile: getNotifications')
    for notification in notifications:
        print(f"Title: {notification['title']}")
        print(f"Text: {notification['text']}")

    success_pn = wait_until_visible_xpath(single_driver_permission_true, "android:id/message")
    assert success_pn.is_displayed()
    click_by_text(single_driver_permission_true, "OK")

    # open notification panel
    single_driver_permission_true.open_notifications()
    pn = wait_until_text_visible(single_driver_permission_true,
                                 "This is push notification for SQEMP mobile application")
    assert pn.is_displayed()
    single_driver_permission_true.press_keycode(3)

    # image = find_element_by_resource_id(single_driver_permission_true, "android:id/big_picture")
    # assert image.is_displayed()


# PERCOBAAN PERTAMA
def test_send_pn_successfully(headers):
    from data.test_data import apk_path
    emulator = {
        'platformName': 'Android',
        'platformVersion': '13.0',
        'deviceName': 'emulator-5554',
        'app': apk_path,
        'automationName': 'UiAutomator2',
        "newCommandTimeout": 1200,
        'autoGrantPermissions': True,
        'avd': 'Pixel_3a_Tiramisu'
    }

    appium_options = UiAutomator2Options()
    appium_options.load_capabilities(emulator)

    appium_server = f'http://localhost:4723'
    driver = webdriver.Remote(appium_server, options=appium_options)

    single_driver_permission_true = driver
    # mobile secrets setup
    sqemp_mobile_setup(single_driver_permission_true)
    #
    # # register user
    # wait_until_text_visible(single_driver_permission_true, "Input your User Id here")
    # time.sleep(3)
    # find_element_by_text(single_driver_permission_true, "Input your User Id here").send_keys("automation")
    # click_by_text(single_driver_permission_true, "REGISTER PUSH NOTIFICATION")
    #
    # # assert push notification successfully sent from mobile
    # success_popup = wait_until_text_visible(single_driver_permission_true, "Register Push Notification succeeds")
    # assert success_popup.is_displayed()
    # click_by_text(single_driver_permission_true, "OK")
    # time.sleep(10)
    #
    # # trigger push notification API
    # send_push_notif(headers, channel_id, "automation")
    # time.sleep(5)
    #
    # notifications = driver.execute_script('mobile: getNotifications', [])
    # print("Notifications:", notifications)
    #
    # bar_notification = get_notification(single_driver_permission_true)
    # success_pn = wait_until_visible_xpath(single_driver_permission_true, "android:id/message")
    # assert success_pn.is_displayed()
    #
    # click_by_text(single_driver_permission_true, "OK")
    #
    # # open notification panel
    # single_driver_permission_true.open_notifications()
    # pn = wait_until_text_visible(single_driver_permission_true,
    #                              "This is push notification for SQEMP mobile application")
    # assert pn.is_displayed()
    # subprocess.run(["adb", "-s", emulator['deviceName'], "emu", "kill"])

    # image = find_element_by_resource_id(single_driver_permission_true, "android:id/big_picture")
    # assert image.is_displayed()
