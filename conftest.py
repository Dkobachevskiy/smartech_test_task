import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture(scope="function")
def browser():
    capa = DesiredCapabilities.CHROME
    capa["pageLoadStrategy"] = "eager"                                          #изменяем значение ожидания загрузки страницы на "интерактивное"
    browser = webdriver.Chrome(desired_capabilities=capa)
    print("\nstart chrome browser for test..")
    yield browser
    print("\nquit browser..")
    browser.quit()
