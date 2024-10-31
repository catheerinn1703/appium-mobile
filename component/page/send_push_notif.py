from component.data.send_push_notif import client_id, user_id, client_secret, app_id
from component.helper.wait_for_element import wait_for_element
from component.locator.send_push_notif import input_user_id_locator, confirm_register_succeed_locator, \
    register_push_notif_locator, setting_button_locator, save_button_locator, client_id_locator, client_secret_locator, \
    app_id_locator


def set_setting(driver):
    element = wait_for_element(driver, ('xpath', setting_button_locator))
    element.click()

    element = wait_for_element(driver, ('xpath', client_id_locator))
    element.send_keys(client_id)

    element = wait_for_element(driver, ('xpath', client_secret_locator))
    element.send_keys(client_secret)

    element = wait_for_element(driver, ('xpath', app_id_locator))
    element.send_keys(app_id)

    element = wait_for_element(driver, ('xpath', save_button_locator))
    assert element.is_displayed() == True
    element.click()


def set_user_id(driver):
    element = wait_for_element(driver, ('xpath', input_user_id_locator))
    element.send_keys(user_id)

    element = wait_for_element(driver, ('xpath', register_push_notif_locator))
    element.click()

    element = wait_for_element(driver, ('xpath', confirm_register_succeed_locator))
    assert element.is_displayed() == True
    element.click()
