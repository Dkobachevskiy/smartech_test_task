from selenium.webdriver.common.by import By


class YandexPageLocators():
    YANDEX_PAGE_LINK = 'https://yandex.ru/'                                     #ссылка на главную страницу Яндекс
    YANDEX_SEARCH_VALUE = (By.XPATH, '//input[@id="text"]')                     #поисковая строка Яндекс
    YANDEX_SEARCH_TEXT = 'расчет расстояний между городами'                     #текст для поиска
    YANDEX_SEARCH_BUTTON = (By.CSS_SELECTOR, 'div .search2__button')            #кнопка "найти" на странице Яндекс


class AutodispetcherPageLocators():
    AUTODISPETCHER_LINK = (                                                     #элемент с ссылкой сайта Автодиспетчер
        By.XPATH,
        '//a[@target="_blank" and @href="https://www.avtodispetcher.ru/distance/"]'
    )
    CALCULATE_BUTTON = (By.XPATH, '//input[@value="Рассчитать"]')               #кнопка для подсчета результата
    CONSAMPTION_FUEL = '9'                                                      #расход топлива
    CONSUMPTION_FUEL_VALUE = (By.XPATH, '//input[@name="fc"]')                  #поле для ввода расхода топлива
    EXPECTED_DISTANCE = '897'                                                   #ожидаемое расстояние
    EXPECTED_DISTANCE_AFTER_UPDATE = '966'                                      #ожидаемое расстояние после добавления еще одного города
    EXPECTED_FUEL_COST = '3726 руб'                                             #ожидаемая стоимость бензина
    EXPECTED_FUEL_COST_AFTER_UPDATE = '4002 руб'                                #ожидаемая стоимость бензина после добавления еще одного города
    FROM_CITY = 'Тула'                                                          #город отправления
    FROM_VALUE = (By.XPATH, '//input[@name="from"]')                            #поле ввода города отправление
    PRICE_FUEL = '46'                                                           #стоимость топлива
    PRICE_FUEL_VALUE = (By.XPATH, '//input[@name="fp"]')                        #поле ввода стоимости топлива
    RESULT_DISTANCE = (By.XPATH, '//span[@id="totalDistance"]')                 #полученное расстояние
    RESULT_FUEL_COST = (By.XPATH, '//div[@id="summaryContainer"]/form/p')       #полученная стоимость топлива
    SET_UP_BUTTON = (By.XPATH, '//a[@id="triggerFormD"]')                       #кнопка "настроить маршрут"
    SET_UP_CONSAMPTION_FUEL_VALUE = (By.XPATH, '//input[@id="f_fc"]')           #поле для ввода нового расхода топлива
    SET_UP_PRICE_FUEL_VALUE = (By.XPATH, '//input[@id="f_fp"]')                 #поле для ввода новой стоимости топлива
    THROUGH_THE_CITY = 'Великий Новгород'                                       #город через который надо проехать
    THROUGH_THE_CITY_VALUE = (By.XPATH, '//input[@name="v"]')                   #поле для ввода города, через который надо проехать
    UPDATE_CALCULATIONS_BUTTON = (                                              #кнопка "обновить расчет"
        By.XPATH, '//input[@value="Обновить расчет"]'
    )
    WHERE_CITY = 'Санкт-Петербург'                                              #город назначения
    WHERE_VALUE = (By.XPATH, '//input[@name="to"]')                             #поле ввода города назначения
