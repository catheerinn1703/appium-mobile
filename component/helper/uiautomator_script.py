def get_notification(driver):
    data = driver.execute_script("mobile: getNotifications")

    return data
