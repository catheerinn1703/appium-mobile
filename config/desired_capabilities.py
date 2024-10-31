from appium import webdriver

from data.test_data import apk_path


def multiple_emulators():
    android13 = {}
    android13['platformName'] = 'Android'
    android13['platformVersion'] = '13.0'
    android13['deviceName'] = 'emulator-5554'
    android13['app'] = apk_path
    android13['automationName'] = 'UiAutomator2'
    android13['appPackage'] = 'com.pushnotificationexample'
    android13['fullReset'] = True
    android13['newCommandTimeout'] = 3000
    android13['autoGrantPermissions'] = True
    android13['avd'] = 'Pixel_3a_Tiramisu'

    android6 = {}
    android6['platformName'] = 'Android'
    android6['platformVersion'] = '6.0'
    android6['deviceName'] = 'emulator-5554'
    android6['app'] = apk_path
    android6['automationName'] = 'UiAutomator2'
    android6['appPackage'] = 'com.pushnotificationexample'
    android6['fullReset'] = True
    android6['newCommandTimeout'] = 3000
    android6['avd'] = 'AVD_6'
    android6['idleTimeout'] = 1200
    android6['adbExecTimeout'] = 3000

    return [android13, android6]


def android_13():
    desired_cap = {}
    desired_cap['platformName'] = 'Android'
    desired_cap['platformVersion'] = '13.0'
    desired_cap['deviceName'] = 'emulator-5554'
    desired_cap['app'] = apk_path
    desired_cap['automationName'] = 'UiAutomator2'
    desired_cap['appPackage'] = 'com.pushnotificationexample'
    desired_cap['appActivity'] = '.MainActivity'
    desired_cap['fullReset'] = False
    desired_cap['newCommandTimeout'] = 6000
    desired_cap['autoGrantPermissions'] = True
    desired_cap['avd'] = 'Pixel_3a_Tiramisu'
    desired_cap['printPageSourceOnFindFailure'] = True
    desired_cap['notifications'] = True
    desired_cap['enableNotificationListener'] = True
    desired_cap['permissions'] = [
        'android.permission.POST_NOTIFICATIONS'
        # 'android.permission.RECEIVE_BOOT_COMPLETED',
        # 'android.permission.VIBRATE',
        # 'android.permission.WAKE_LOCK',
        # 'android.permission.ACCESS_NOTIFICATIONS',
        # 'android.permission.ACCESS_NOTIFICATION_POLICY',
        # 'android.permission.BIND_NOTIFICATION_LISTENER_SERVICE'
    ]

    return desired_cap


def android_6():
    desired_cap = {}
    desired_cap['platformName'] = 'Android'
    desired_cap['platformVersion'] = '6.0'
    desired_cap['deviceName'] = 'emulator-5554'
    desired_cap['app'] = apk_path
    desired_cap['automationName'] = 'UiAutomator2'
    desired_cap['appPackage'] = 'com.pushnotificationexample'
    desired_cap['appActivity'] = 'com.pushnotificationexample.MainActivity'
    desired_cap['fullReset'] = True
    desired_cap['newCommandTimeout'] = 3000
    desired_cap['avd'] = 'AVD_6'
    desired_cap['idleTimeout'] = 1200
    desired_cap['printPageSourceOnFindFailure'] = True

    return desired_cap


def emulator_os_5():
    return {
        'platformName': 'Android',
        'platformVersion': '5.0',
        'deviceName': 'emulator-5556',
        'app': apk_path,
        'automationName': 'UiAutomator2',
        'appPackage': 'com.pushnotificationexample',
        'fullReset': True,
        'newCommandTimeout': 3000,
        'autoGrantPermissions': True,
        'avd': 'Google_5',
        'idleTimeout': 1200
    }
