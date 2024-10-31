from data.test_data import mp_client_id, mp_client_secret, mp_app_id
from tests.function.base import click_by_text, find_element_by_hint, click_save, wait_until_text_visible, \
    find_element_by_text


def sqemp_mobile_setup(driver):
    click_by_text(driver, "Settings")
    wait_until_text_visible(driver, "Client Id")
    find_element_by_text(driver, "e5e3b10156de7c29").send_keys(mp_client_id)
    find_element_by_text(driver, "63713d3dd7b93b6a").send_keys(mp_client_secret)
    find_element_by_text(driver, "sqemp").send_keys(mp_app_id)
    click_save(driver)

#
# def click_allow_button_if_visible(driver):
