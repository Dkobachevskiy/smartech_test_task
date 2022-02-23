from .pages.base_page import BasePage
from .pages.locators import AutodispetcherPageLocators, YandexPageLocators


def test_can_create_and_changing_route(browser):                                #тест проверки возможности перехода на сайт автодиспетчер с выдачи Яндекса и выполнения необходимых действий
    yandex_link = YandexPageLocators.YANDEX_PAGE_LINK
    page = BasePage(browser, yandex_link)                                       #создаем объект страницы
    page.open()                                                                 #открываем ссылку страницы яндекса
    page.entering_request_in_value(                                             #вводим запрос на поиск в поисковую строку
        YandexPageLocators.YANDEX_SEARCH_TEXT,
        YandexPageLocators.YANDEX_SEARCH_VALUE
    )
    page.push_on_button(YandexPageLocators.YANDEX_SEARCH_BUTTON)                #нажимаем на кнопку найти
    page_url = browser.current_url                                              #получаем  url страницы на которой находимся
    page.is_element_present(                                                    #проверяем в выдаче яндекса наличие сайта автодиспетчер
        AutodispetcherPageLocators.AUTODISPETCHER_LINK,
        page_url
    )
    page.open_page(AutodispetcherPageLocators.AUTODISPETCHER_LINK)              #переходим на сайт автодиспетчер
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    page_url = browser.current_url                                              #обновляем адрес страницы
    page.is_element_present(                                                    #проверяем наличие поля для ввода города отправления
        AutodispetcherPageLocators.FROM_VALUE,
        page_url
    )
    page.entering_request_in_value(                                             #вводим город отправления
        AutodispetcherPageLocators.FROM_CITY,
        AutodispetcherPageLocators.FROM_VALUE
    )
    page.is_element_present(                                                    #проверяем наличие поля для ввода города назначения
        AutodispetcherPageLocators.WHERE_VALUE,
        page_url
    )
    page.entering_request_in_value(                                             #вводим город назначения
        AutodispetcherPageLocators.WHERE_CITY,
        AutodispetcherPageLocators.WHERE_VALUE
    )
    page.is_element_present(                                                    #проверяем наличие поля для ввода стоимости топлива
        AutodispetcherPageLocators.PRICE_FUEL_VALUE,
        page_url
    )
    page.entering_request_in_value(                                             #задаем необхоимую стоимость топлива
        AutodispetcherPageLocators.PRICE_FUEL,
        AutodispetcherPageLocators.PRICE_FUEL_VALUE
    )
    page.is_element_present(                                                    #проверяем наличие поля для ввода рахода топлива
        AutodispetcherPageLocators.CONSUMPTION_FUEL_VALUE,
        page_url
    )
    page.entering_request_in_value(                                             #вводим значение расхода топлива
        AutodispetcherPageLocators.CONSAMPTION_FUEL,
        AutodispetcherPageLocators.CONSUMPTION_FUEL_VALUE
    )
    page.move_to_element(AutodispetcherPageLocators.CALCULATE_BUTTON)
    page.push_on_button(AutodispetcherPageLocators.CALCULATE_BUTTON)            #нажимаем на кнопку подсчета значений
    page_url = browser.current_url                                              #щбновляем адрес страницы
    page.cheking_result(                                                        #сравниваем полученный результат расстояния с ожидаемым
        AutodispetcherPageLocators.EXPECTED_DISTANCE,
        AutodispetcherPageLocators.RESULT_DISTANCE,
        page_url
    )
    page.cheking_result(                                                        #сравниваем полученный результат стоимости топлива с ожидаемым
        AutodispetcherPageLocators.EXPECTED_FUEL_COST,
        AutodispetcherPageLocators.RESULT_FUEL_COST,
        page_url
    )
    page.is_element_present(                                                    #проверяем наличие кнопки "настроить маршрут" на странице
        AutodispetcherPageLocators.SET_UP_BUTTON,
        page_url
    )
    page.push_on_button(AutodispetcherPageLocators.SET_UP_BUTTON)               #нажимаем "настроить маршрут"
    page_url = browser.current_url
    page.is_element_present(                                                    #проверяем наличие поля для ввода города, через который надо проехать
        AutodispetcherPageLocators.THROUGH_THE_CITY_VALUE,
        page_url
    )
    page.entering_request_in_value(                                             #вводим город, через который надо проехать
        AutodispetcherPageLocators.THROUGH_THE_CITY,
        AutodispetcherPageLocators.THROUGH_THE_CITY_VALUE
    )
    page.move_to_element(AutodispetcherPageLocators.CALCULATE_BUTTON)
    page.push_on_button(AutodispetcherPageLocators.CALCULATE_BUTTON)            #нажимаем на кнопку подсчета результатов
    page_url = browser.current_url
    page.cheking_result(                                                        #сравниваем полученный результат расстояния с ожидаемым
        AutodispetcherPageLocators.EXPECTED_DISTANCE_AFTER_UPDATE,
        AutodispetcherPageLocators.RESULT_DISTANCE,
        page_url
    )
    page.cheking_result(                                                        #сравниваем полученный результат стоимости топлива с ожидаемым
        AutodispetcherPageLocators.EXPECTED_FUEL_COST_AFTER_UPDATE,
        AutodispetcherPageLocators.RESULT_FUEL_COST,
        page_url
    )
