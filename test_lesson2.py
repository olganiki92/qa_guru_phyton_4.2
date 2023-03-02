import pytest
from selene import browser
from selene.support.conditions import be, have


@pytest.fixture()
def config_browser ():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    return browser



def test_google_find_positive(config_browser):
    browser.open('https://www.google.com/')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_find_negative(config_browser):
    browser.open('https://www.google.com/')
    browser.element('[name="q"]').should(be.blank).type('drdghddth').press_enter()
    browser.element('.card-section').should(have.text('По запросу drdghddth ничего не найдено.'))